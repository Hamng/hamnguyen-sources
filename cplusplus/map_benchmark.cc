// To build:
//	make CXXFLAGS='-O3 -std=c++11' LDLIBS='-lcrypto -lpthread' map_benchmark
//	Add '-ljemalloc' if wanting to link with the jemalloc library
// Don't even need a Makefile!
// Too bad, C++11 doesn't support some needed features
//	(e.g. can't use "auto" in function declaration),
//	so really need a newer C++, do:
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

using namespace std;


template <typename KeyType, typename ValueType>
class MyThreadObject {
  public:
    static void launch_threads(const size_t num_threads, const size_t num_pairs);
    static void thread_entry(MyThreadObject * const);

    static int		verbosity;

  protected:
    virtual void run();

    thread *		pthread;		// "p" is for pointer
    unsigned int	thread_num;		// a small unique uint to distinguish threads
    unsigned int	cpu;			// the CPU# a thread runs on

    size_t		num_pairs;		// num of Key/Value pairs
    size_t		map_size;		// size of resulting map
    double		num_seconds;		// #seconds
};


template <typename K, typename V>
int MyThreadObject<K,V>::verbosity = 2;


template <typename K, typename V>
void
MyThreadObject<K,V>::thread_entry(MyThreadObject<K,V> *const pthr)
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
	     << pthr->cpu << endl;
    }

    pthr->run();

    // Note: if a thread calls pthread_exit(), it will NOT reach here!

    if (verbosity > 2) {
	cout << " Thread #" << pthr->thread_num << ": finishes running on CPU #"
	     << pthr->cpu << endl;
    }
}


template <typename K, typename V>
void
MyThreadObject<K,V>::launch_threads(const size_t num_threads,
				    const size_t num_pairs)
{
    auto start = chrono::high_resolution_clock::now();

    MyThreadObject<K,V> thread_array[num_threads];

    if (verbosity > 1) {
	cout << "Creating/launching " << num_threads << " threads:" << endl;
    }

    for (auto &thr : thread_array) {
	// Assign each thread a unique small uint to distinguish
	thr.thread_num = (&thr - &thread_array[0]) + 1;
	thr.num_pairs  = num_pairs;
	if (verbosity > 3) {
	    cout << "  Thread #" << thr.thread_num << ": being created/launched" << endl;
	}
	thr.pthread = new thread(thread_entry, &thr);
    }

    if (verbosity > 1) {
	cout << "Waiting for " << num_threads << " threads to join..." << endl;
    }

    for (auto &thr : thread_array) {
        thr.pthread->join();
	delete thr.pthread;
	if (verbosity > 3) {
	    cout << "  Thread #" << thr.thread_num << ": ran on CPU #" << thr.cpu << endl;
	}
	if (verbosity > 1) {
	    cout << "Thread #" << thr.thread_num << " (CPU #" << thr.cpu
		 << "): " << thr.map_size << " pairs were map::insert'ed in "
		 << fixed << setprecision(4) << thr.num_seconds << "secs" << endl;
	}
    }

    auto finish = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = finish - start;

    if (verbosity > 1) {
	cout << "All " << num_threads << " threads joined." << endl
	     << "Total elapsed time: " << fixed << setprecision(4)
	     << elapsed.count() << "secs" << endl;
    }
}



// This is the gut of what's going to be done within each thread
template <typename K, typename V>
void
MyThreadObject<K,V>::run()
{
    K * keys   = new K[num_pairs];
    V * values = new V[num_pairs];
    K * pk;
    V * pv;
    int i, res;

    res = RAND_bytes((unsigned char *) keys, num_pairs * sizeof(K));
    if (verbosity > 2) {
	cout << " Thread #" << thread_num << " (CPU #" << cpu
	     << "): RAND_bytes(keys, " << num_pairs
	     << " * " << sizeof(K) << ") returned " << res << endl;
    }

    res = RAND_bytes((unsigned char *) values, num_pairs * sizeof(V));
    if (verbosity > 2) {
	cout << " Thread #" << thread_num << " (CPU #" << cpu
	     << "): RAND_bytes(values, " << num_pairs
	     << " * " << sizeof(V) << ") returned " << res << endl;
    }

    map<K, V> kv_map;

    auto start = chrono::high_resolution_clock::now();

    for (i = 0, pk = keys, pv = values; i < num_pairs; i++, ++pk, ++pv) {
	kv_map.insert({*pk, *pv});		// don't replace dup key
	//kv_map[*pk] = *pv;			// do	 replace
    }

    auto finish = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = finish - start;
    num_seconds = elapsed.count();

    map_size = kv_map.size();
    if (verbosity > 2) {
    	cout << " Thread #" << thread_num << " (CPU #" << cpu
	     << "): " << map_size << " pairs were map::insert'ed in "
	     << fixed << setprecision(4) << num_seconds << "secs" << endl;
    }
    kv_map.clear();

    delete keys;
    delete values;
}




int
main(int argc, char *argv[])
{
    const auto num_threads = (argc < 2) ? 8 : atoi(argv[1]);

    const auto num_pairs   = (argc < 3) ? 100 : atoi(argv[2]);

    const bool key_is_str  = ((argc < 4) ? 0 : atoi(argv[3])) & 1;
    const bool val_is_str  = ((argc < 5) ? 0 : atoi(argv[4])) & 1;

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

    if (key_is_str && val_is_str) {
	MyThreadObject<string, string>::launch_threads(num_threads, num_pairs);
    } else if (key_is_str && ! val_is_str) {
	MyThreadObject<string, int>::launch_threads(num_threads, num_pairs);
    } else if (! key_is_str && val_is_str) {
	MyThreadObject<int, string>::launch_threads(num_threads, num_pairs);
    } else {
	MyThreadObject<int, int>::launch_threads(num_threads, num_pairs);
    }

    return 0;
}
