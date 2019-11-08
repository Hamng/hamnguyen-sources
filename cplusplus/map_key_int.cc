// To build (don't even need a Makefile!):
//	make CXXFLAGS='-O3 -std=c++11' LDLIBS='-lcrypto -lpthread' map_key_int
//	To link with the jemalloc library:
//	   a.	Append '-ljemalloc' to LDLIBS=
//	   b.	Bonus: if wanting to show Jemalloc stats when program exits,
//		setenv MALLOC_CONF=stats_print:true before execution
// Too bad, C++11 doesn't support some needed features
//	(e.g. can't use "auto" in function declaration),
//	so if really need a newer-than-C++11, do:
//	scl  enable  devtoolset-8  bash
//	make  CXXFLAGS='-O3 -std=c++17'  ...


#include <iostream>
#include <iomanip>
#include <thread>
#include <sched.h>
#include <stdlib.h>
#include <openssl/engine.h>
#include <openssl/rand.h>
#include <map>
#include <chrono>
#include <unistd.h>				// sleep()

using namespace std;


class MyThreadObject {
  public:
    static void		thread_entry(MyThreadObject * const);

    static int		verbosity;

  protected:
    //MyThreadObject(const size_t nthreads);
    //virtual ~MyThreadObject();

    virtual void 	run() = 0;

    thread *		pthread;		// "p" is for pointer
    unsigned int	thread_num;		// a small unique uint to distinguish threads
    unsigned int	cpu;			// the CPU# a thread runs on
};


class ValueObject: public MyThreadObject {
  public:
    //typedef struct {unsigned long value[8];} ValueType;
    typedef unsigned long ValueType;

    static void launch_threads(ValueObject *const thread_array,
			       const size_t num_threads,
			       const size_t num_pairs);

  protected:
    //virtual ~ValueObject();

    size_t		map_size;		// size of resulting map
    double		num_seconds;		// #seconds

    static ValueType *	values;
    static size_t	num_pairs;		// num of Key/Value pairs
};


class KeyObject_4 : public ValueObject {
  public:
    typedef unsigned int KeyType;
    typedef map<KeyType, ValueType> KeyValueType;

  protected:
    virtual void 	run() override;
    KeyType *		keys;
    KeyValueType	key_value;
};


int MyThreadObject::verbosity = 4;

ValueObject::ValueType *ValueObject::values  = NULL;
size_t ValueObject::num_pairs = 0;

#if 0
MyThreadObject::MyThreadObject(const size_t nthreads)
    : num_threads(nthreads), thread_array(NULL)
{
}

MyThreadObject::~MyThreadObject()
{
    for (auto i = num_threads; i--;) {
	delete thread_array[i].pthread;		// in case it wasn't deleted yet
    }
    delete thread_array;
}

ValueObject::ValueObject(const size_t nthreads, const size_t npairs)
    : MyThreadObject(nt), num_pairs(npairs)
{
    values = new ValueObject[num_pairs];
}


ValueObject::~ValueObject()
{
    delete values;			// in case it wasn't deleted yet
}


KeyObject_4::KeyObject_4(const size_t nthreads, const size_t npairs)
    : ValueObject(nthreads, npairs)
{
    thread_array = new KeyObject_4[nthreads];
}
#endif


void
MyThreadObject::thread_entry(MyThreadObject *const pthr)
{
#ifdef __gnu_linux__
    pthr->cpu = sched_getcpu();
#else
    pthr->cpu = 0;
#endif

    // If wanting to give other threads a chance to be launched/started,
    // then uncomment the code below to wait a bit.
    //sleep(pthr->thread_num);

    // Note: stdout is going to be severely intermixed -- even on a single line so
    // would need a mechanism to serialize stdout (i.e. each thread completes its line).

    if (verbosity > 2) {
	cout << " Thread #" << pthr->thread_num << ": starts running on CPU #"
<< "@" << pthr << ", #"
	     << pthr->cpu << endl;
    }

    pthr->run();

    // Note: if a thread calls pthread_exit(), it will NOT reach here!

    if (verbosity > 2) {
	cout << " Thread #" << pthr->thread_num << ": finishes running on CPU #"
	     << pthr->cpu << endl;
    }
}


void
ValueObject::launch_threads(ValueObject *const thread_array,
			    const size_t num_threads,
			    const size_t npairs)
{
    auto start = chrono::high_resolution_clock::now();
    auto i = num_threads;
    auto pthr = thread_array;

    num_pairs = npairs;
    values = new ValueType[num_pairs];
    int res = RAND_bytes((unsigned char *) values, num_pairs * sizeof(*values));
    if (verbosity > 2) {
	cout << "RAND_bytes(values[], " << num_pairs
	     << " * " << sizeof(*values) << ") returned " << res << endl;
    }

    if (verbosity > 1) {
	cout << "Creating/launching " << num_threads << " threads:" << endl;
    }

    for (i = 0, pthr = thread_array; i < num_threads; i++, pthr++) {
	// Assign each thread a unique small uint to distinguish
	pthr->thread_num = i + 1;
	if (verbosity > 3) {
	    cout << "  Thread #" << pthr->thread_num
<< "@" << pthr
		 << ": being created/launched" << endl;
	}
	pthr->pthread = new thread(thread_entry, pthr);
pthr->pthread->join();
sleep(5);
    }

    if (verbosity > 1) {
	cout << "Waiting for " << num_threads << " threads to join..." << endl;
    }

    for (i = num_threads, pthr = thread_array; i--; pthr++) {
        pthr->pthread->join();
	//delete pthr->pthread;
	//pthr->pthread = NULL;
	if (verbosity > 3) {
	    cout << "  Thread #" << pthr->thread_num
		 << ": ran on CPU #" << pthr->cpu << endl;
	}
	if (verbosity > 1) {
	    cout << "Thread #" << pthr->thread_num << " (CPU #" << pthr->cpu
		 << "): " << pthr->map_size << " pairs were map::insert'ed in "
		 << fixed << setprecision(4) << pthr->num_seconds
		 << "secs" << endl;
	}
    }

    auto finish = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = finish - start;

    if (verbosity > 1) {
	cout << "All " << num_threads << " threads joined." << endl
	     << "Total elapsed time: " << fixed << setprecision(4)
	     << elapsed.count() << "secs" << endl;
    }

    delete values;
    values = NULL;
}


// This is the gut of what's going to be done within each thread
void
KeyObject_4::run()
{
cerr << __func__ << "(): this@" << this << endl;
    int i, res;
    keys    = new KeyType[num_pairs];
    auto pk = keys;
    auto pv = values;

    res = RAND_bytes((unsigned char *) keys, num_pairs * sizeof(*keys));
    if (verbosity > 2) {
	cout << " Thread #" << thread_num << " (CPU #" << cpu
<< " {@" << this << ", keys@" << keys << "}"
	     << "): RAND_bytes(keys[], " << num_pairs
	     << " * " << sizeof(*keys) << ") returned " << res << endl;
    }

    auto start = chrono::high_resolution_clock::now();

    for (auto i = num_pairs; i--; ++pk, ++pv) {
	key_value.insert({*pk, *pv});	// don't replace dup key
	//key_value[*pk] = pv->value;		// do	 replace
    }

    auto finish = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = finish - start;
    num_seconds = elapsed.count();

    map_size = key_value.size();
    if (verbosity > 2) {
    	cout << " Thread #" << thread_num << " (CPU #" << cpu
	     << "): " << map_size << " pairs were map::insert'ed in "
	     << fixed << setprecision(4) << num_seconds << "secs" << endl;
    }
    key_value.clear();

    delete keys;
}




int
main(int argc, char *argv[])
{
    const auto num_threads = (argc < 2) ? 8 : atoi(argv[1]);

    // On aarch64 with 8G mem (no swap), num_pairs > 31k would crash jemalloc;
    // probably out-of-memory
    const auto num_pairs  = (argc < 3) ? 10000000 : atoi(argv[2]);

    const size_t key_size = (argc < 4) ? sizeof(KeyObject_4::KeyType) : atoi(argv[3]);

    ENGINE *engine;
    ENGINE_load_rdrand();
    engine = ENGINE_by_id("rdrand");
    if (engine == NULL) {
	// Hmm, the "rdrand" engine seems to work only on some x86_64
	// and not on others, and not on ARM.
	// But that seems to be a soft failure, so don't exit()
	cerr << "ENGINE_by_id(\"rdrand\") returned "
	     << ERR_get_error() << endl;
	//exit(1);
    } else {
	if ( ! ENGINE_init(engine) ) {
	    cerr << "ENGINE_init returned " << ERR_get_error() << endl;
	    exit(1);
	}

	if ( ! ENGINE_set_default(engine, ENGINE_METHOD_RAND) ) {
	    cerr << "ENGINE_set_default(*, ENGINE_METHOD_RAND) returned "
		 << ERR_get_error() << endl;
	    exit(1);
	}
    }

    switch (key_size) {
	case sizeof(KeyObject_4::KeyType):
	default:
	    KeyObject_4 * thread_array = new KeyObject_4[num_threads];
	    ValueObject::launch_threads(thread_array, num_threads, num_pairs);
	    break;
    }

    return 0;
}
