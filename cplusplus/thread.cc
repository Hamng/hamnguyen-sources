// To build (don't even need a Makefile!):
//	make  CXXFLAGS='-std=c++11'  LDLIBS='-lpthread'  <this_file_no_suffix>
//	To link with the jemalloc library:
//	   a.	Append '-ljemalloc' to LDLIBS=
//	   b.	Bonus: if wanting to show Jemalloc stats when program exits,
//		setenv MALLOC_CONF=stats_print:true before execution
// Too bad, C++11 doesn't support some needed features
//	(e.g. can't use "auto" in function declaration),
//	so if really need a newer-than-C++11, do:
//	scl  enable  devtoolset-8  bash
//	make  CXXFLAGS='-std=c++17'  ...
// To keep everything in a single file:
//	MyThreadObject::run(): implement it here, then 'make' as above
// To split to multiple files:
//  1.	my_thread.hh: already there.
//  2.	MyThreadObject::run(): implement it in a separate my_thread_run.cc.
//  3.	make  CXXFLAGS='-std=c++11 -DMY_THREAD_EXTERNAL'  <this_file_no_suffix>.o  my_thread_run.o
//	${CXX:-g++}  -o <this_file_no_suffix>  *.o  -lpthread


#include <iostream>
#include <thread>
#include <sched.h>
#include <stdlib.h>
#include <unistd.h>				// sleep()

using namespace std;


#if defined(MY_THREAD_EXTERNAL)

#include "my_thread.hh"

#else

class MyThreadObject {
  public:
    static void launch_threads(const size_t num_threads);

    static int		verbosity;

  protected:
    void thread_entry();
    virtual void run();

    thread *		pthread;
    unsigned int	thread_num;		// a small unique uint to distinguish threads
    unsigned int	cpu;			// the CPU# a thread runs on
};

#endif


int MyThreadObject::verbosity = 4;


void
MyThreadObject::thread_entry()
{
#ifdef __gnu_linux__
    cpu = sched_getcpu();
#else
    cpu = 0;
#endif

    // If wanting to give other threads a chance to be launched/started,
    // then uncomment the code below to wait a bit.
    //sleep(thread_num);

    // Note: stdout is going to be severely intermixed -- even on a single line so
    // would need a mechanism to serialize stdout (i.e. each thread completes its line).

    if (verbosity > 2) {
	cout << " Thread #" << thread_num << ": starts running on CPU #"
	     << cpu << endl;
    }

    run();

    // Note: if a thread calls pthread_exit(), it will NOT reach here!

    if (verbosity > 2) {
	cout << " Thread #" << thread_num << ": finishes running on CPU #"
	     << cpu << endl;
    }
}


void
MyThreadObject::launch_threads(const size_t num_threads)
{
    MyThreadObject thread_array[num_threads];

    if (verbosity > 1) {
	cout << "Creating/launching " << num_threads << " threads:" << endl;
    }

    for (auto &thr : thread_array) {
	// Assign each thread a unique small uint to distinguish
	thr.thread_num = (&thr - &thread_array[0]) + 1;
	if (verbosity > 3) {
	    cout << "  Thread #" << thr.thread_num << ": being created/launched" << endl;
	}
	thr.pthread = new thread(&MyThreadObject::thread_entry, thr);
    }

    if (verbosity > 1) {
	cout << "Waiting for " << num_threads << " threads to join..." << endl;
    }

    for (auto &thr : thread_array) {
        thr.pthread->join();
	if (verbosity > 3) {
	    cout << "  Thread #" << thr.thread_num << ": ran on CPU #" << thr.cpu << endl;
	}
	delete thr.pthread;
    }

    if (verbosity > 1) {
	cout << "All " << num_threads << " threads joined" << endl;
    }
}



#if !defined(MY_THREAD_EXTERNAL)

// This is the gut of what's going to be done within each thread
void
MyThreadObject::run()
{
}

#endif


int
main(int argc, char *argv[])
{
    const size_t nthreads = (argc < 2) ? 8 : atoi(argv[1]);

    MyThreadObject::launch_threads(nthreads);

    return 0;
}
