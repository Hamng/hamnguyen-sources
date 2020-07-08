// Prerequisite: TCLAP (Templatized C++ Command Line Parser)
// The easiest way is to unpack a TCLAP tarball, then copy or symlink
// the <tcltap-ver>/include/tclap/ to the same dir containing this source
// To benchmark a tracefile using Collaborative Sort
// To build: g++ --std=c++1y -I<path/to/tclap/include> collaborative_sort_benchmark.cc
// Need to use C++17 "for (auto e : v) ..."
// Hmm, --std=c++0x compiles ok too

#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>

#include <stdio.h>

//#include <experimental/iterator>	NOT working with GCC 4.8.5
#include "tclap/CmdLine.h"

#include "configManager.hh"

#if !defined(KEYSIZE)
#define	KEYSIZE		24
#endif

#if !defined(MAXVALUESIZE)
#define	MAXVALUESIZE	((size_t) (1 << 16))
//#define MAXVALUESIZE	((size_t) (1 << 9))
#endif

#if !defined(DISK_SIZE)
#define	DISK_SIZE	((size_t) (1 << 7))
#endif

#if !defined(REPORT_INTVL)
// every 100,000 requests
#define	REPORT_INTVL	(100 * 1000)
#endif


using namespace std;
//using namespace std::string_literals;		Sigh! NOT working for G++ 4.8.5
//using namespace TCLAP;

const static string version("0.4");
static bool verbose = true;
static bool dryrun = false;
static bool verify = false;


static const char *
enabled_disabled_str(const bool f)
{
    static const char * enabled_str  = "enabled";
    static const char * disabled_str = "disabled";
    return (f ? enabled_str : disabled_str);
}


static void
validate_tracefile(const string &filename, size_t &numPairs, const size_t ratio)
{
    // verify that the tracefile exists and readable
    ifstream ifs(filename);
    if (! ifs) {
	throw ios_base::failure(string("Can't open tracefile '") 
				+ filename + string("' for reading"));
    }

    // Parse for ValueSize as the 1st (comma-separated) field in the 1st line
    size_t valueSize = 0;
    ifs >> valueSize;
    if (verbose) {
	cout << "Tracefile: " << filename << endl;
	cout << "ValueSize (1st field in 1st line in tracefile): " << valueSize << endl;
    }
    if (valueSize >= MAXVALUESIZE) {
	// abort if too large
	stringstream errMsg;
	errMsg << "ValueSize=" << valueSize
	       << " >= compiled-in MAXVALUESIZE=" << MAXVALUESIZE;
	throw runtime_error(errMsg.str());
    }

    ifs.close();

    if (numPairs) {
	if (verbose) {
	    cout << "# of Key-Value pairs: " << numPairs << endl;
	}
    } else {
	// numPairs wasn't explicitly specified so set it to lineCount / ratio
	FILE *fp = popen((string("wc -l < ") + filename).c_str(), "r");
	size_t lineCount;
	fscanf(fp, "%zu", &lineCount);
	pclose(fp);
	numPairs = lineCount / ratio;
	if (verbose) {
	    cout << "# of Key-Value pairs: " << numPairs
		 << " (== " << lineCount
		 << " / " << ratio << ")" << endl;
	}
    }
}


static void
process_config_file(const string &configFile)
{
    // verify that the config file exists and readable
    ifstream ifs(configFile);
    if (! ifs) {
	throw ios_base::failure(string("Can't open config file '")
				+ configFile + string("' for reading"));
    }
    ifs.close();

    if (verbose) {
	cout << "Config: " << configFile << endl;
    }

    // init configManager
    ConfigManager::getInstance().setConfigPath(configFile.c_str());
}


static void *
create_disks(void *d, const vector<string> &dirs, const size_t diskGSize)
{
    // Should verify that each member of dirs is a directory
    // and dirs.size() > 0 (already implicitly checked by TCLAP)
    if (verbose) {
	cout << "Disk size: " << diskGSize << "GiB" << endl;
	cout << dirs.size() << " director(ies): ";

	// Too bad, below is the C++17 fancy way to show the entire vector
	// but can't find #include <experimental/iterator>, sigh!
	//copy(dirs.begin(), dirs.end(),
	//     experimental::make_ostream_joiner(cout, " "));

	for (auto d : dirs) {
	    cout << d << " ";
	}
	cout << endl;
    }

    //for(i = 0 ; i < numDisks ; i++){
    //    DiskInfo *disk = new DiskInfo(i,diskPaths[i],DISK_SIZE);
    //    disks->push_back(*disk);
    //}

    return NULL;
}


int
main(int argc, char** argv)
{
    string traceFile;
    string configFile;
    size_t numPairs;
    size_t ratio = 0;	// Hmm, must inir to avoid -Werror=maybe-uninitialized
    size_t diskGSize;
    size_t reportInterval;
    vector<string> dirs;

    // Wrap everything in a try block.  Do this every time,
    // because exceptions will be thrown for problems.
    try {

	// Define the command line object, and insert a message
  	// that describes the program. The "Command description message"
  	// is printed last in the help text. The second argument is the
  	// delimiter (usually space) and the last one is the version number.
  	// The CmdLine object parses the argv array based on the Arg objects
  	// that it contains.
	// Caveat: Sigh! USAGE shows options in reverse order of calling cmd.add();
	// i.e. 1st cmd.add() will be shown last, and vice versa.
	// Except for Unlabeled whose Usage is always shown last
  	TCLAP::CmdLine
	    cmd("Benchmark a specified tracefile using Collaborative Sort",
		' ', version);

  	// Define a switch and add it to the command line.
  	// A switch arg is a boolean argument and only defines a flag that
  	// indicates true or false.  In this example the SwitchArg adds itself
  	// to the CmdLine object as part of the constructor.  This eliminates
  	// the need to call the cmd.add() method.  All args have support in
  	// their constructors to add themselves directly to the CmdLine object.
  	// It doesn't matter which idiom you choose, they accomplish the same thing.
  	TCLAP::SwitchArg
	    verboseSwitch("", "verbose",
			  (string("If enabled, produce verbose output. Default: ")
			   + string(enabled_disabled_str(verbose))).c_str(),
			  cmd, verbose);

  	TCLAP::SwitchArg
	    dryrunSwitch("", "dryrun",
			 (string("If enabled, does a dryrun only. Default: ")
			  + string(enabled_disabled_str(dryrun))).c_str(),
			 cmd, dryrun);

  	TCLAP::SwitchArg
	    verifySwitch("", "verify",
			 (string("If enabled, verify read data. Default: ")
			  + string(enabled_disabled_str(verify))).c_str(),
			 cmd, verify);

    	TCLAP::ValueArg<size_t>
	    reportIntervalArg("", "report_interval",
			"Number of requests between each reporting interval. Default: 100K.",
			false, REPORT_INTVL, "integer");
  	cmd.add(reportIntervalArg);

    	TCLAP::ValueArg<size_t>
	    diskGSizeArg("", "disk_gsize",
			"Size of each emulated disk in GiB units. Default: 128GiB.",
			false, DISK_SIZE, "integer");
  	cmd.add(diskGSizeArg);

    	TCLAP::ValueArg<string>
	    configFileArg("", "config",
			  "Path to a config file. Default: config.ini.",
			  false, "config.ini", "config.ini");
  	cmd.add(configFileArg);

    	TCLAP::ValueArg<size_t>
	    ratioArg("r", "ratio",
		     "If the number of Key-Value pairs is not explicitly specified,"
		     " it'll be determined by dividing the number_of_lines"
		     " in the tracefile by this ratio. Default: 6.",
		     false, 6, "integer");
  	cmd.add(ratioArg);

  	TCLAP::ValueArg<size_t>
	    pairsArg("n", "pairs",
		     "Number of Key-Value pairs to benchmark."
		     " (If specified, will disregard the --ratio option below.)",
		     false, 0, "integer");
  	cmd.add(pairsArg);

  	// Define a value argument and add it to the command line.
  	// A value arg defines a flag and a type of value that it expects,
  	// such as "-n Bishop".
  	TCLAP::UnlabeledValueArg<string>
	    traceFileArg("file",
			 "Path to a tracefile to benchmark.",
			 true, "", "tracefile");
  	// Add the argument nameArg to the CmdLine object. The CmdLine object
  	// uses this Arg to parse the command line.
  	cmd.add(traceFileArg);

  	TCLAP::UnlabeledMultiArg<string>
	    dirsArg("dirs",
		    "Director(ies) to emulate the disk(s)."
		    " Each directory should be empty.",
		    true, "directory");
  	cmd.add(dirsArg);


  	// Parse the argv array.
  	cmd.parse(argc, argv);

  	// Get the value parsed by each arg.
  	traceFile  = traceFileArg.getValue();
  	configFile = configFileArg.getValue();
	numPairs   = pairsArg.getValue();
	ratio      = ratioArg.getValue();
	diskGSize  = diskGSizeArg.getValue();
	reportInterval = reportIntervalArg.getValue();
  	verify     = verifySwitch.getValue();
  	dryrun     = dryrunSwitch.getValue();
  	verbose    = verboseSwitch.getValue();
	dirs       = dirsArg.getValue();

    } catch (TCLAP::ArgException &e)  // catch any exceptions
    {
	cerr << "error: " << e.error() << " for arg " << e.argId() << endl;
    }

    try {
	if (reportInterval) {
	    // Noop here so GCC won't complain unused
	}

	validate_tracefile(traceFile, numPairs, ratio);

	process_config_file(configFile);

	// array of data disks
	//vector<DiskInfo> *disks = new vector<DiskInfo>;
	create_disks(NULL, dirs, diskGSize);

	//DeviceManager *diskMod = new DeviceManager(*disks);

	//kvserver = new KvServer(diskMod);

	//FILE fp = fopen(traceFile.c_str(), "r");

    } catch (const char *msg)
    {
	cerr << "Error: " << msg << endl;
    }
}
