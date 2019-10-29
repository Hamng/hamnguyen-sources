// To build:
//	make  CXXFLAGS=-std=c++11  LDLIBS=-lpthread  <this_file_no_suffix>
// Don't even need a Makefile!
// To keep everything in a single file:
//	SimplePthread::run(): implement it here, then 'make' as above
// To split to multiple files:
//  1.	simple_thread.hh: already there.
//  2.	SimplePthread::run(): implement it in a separate *.cc.
//  3.	make  CXXFLAGS=-std=c++11  <this_file_no_suffix>.o  simple_pthread_run.o
//	${CXX:-g++}  -o <this_file_no_suffix>  *.o  -lpthread


#include <iostream>
#include <vector>
#include <pthread.h>
#include <sched.h>
//#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

using namespace std;


#if defined(SIMPLE_PTHREAD_EXTERNAL)

#include "simple_pthread.hh"

#else

class SimplePthread {
  public:
    static void launch_threads(const size_t num_threads);
    static void * thread_entry(void *);

    pthread_t * ptr_to_thread_id()	{return &thread_id;}

    void thread_terminate(void *res);		// For the current thread to self-terminate

    static int		verbosity;

  protected:
    virtual void *run();

    pthread_t		thread_id;		// set by pthread_create()
    unsigned int	thread_num;		// a small unique uint to distinguish threads
    unsigned int	cpu;			// the CPU# a thread runs on
    void *		thread_returned_value;	// to return when a thread exits
};

#endif


int SimplePthread::verbosity = 4;


void
SimplePthread::thread_terminate(void *res)
{
    if (verbosity > 2) {
	cout << " Thread #" << thread_num << ": terminates on CPU #"
	     << cpu << "; returning " << res << endl;
    }

    pthread_exit(thread_returned_value = res);
}


void *
SimplePthread::thread_entry(void *arg)
{
    SimplePthread *pthr = (SimplePthread *) arg;

    pthr->thread_id = pthread_self();
    pthr->cpu = sched_getcpu();

    // If wanting to give other threads a chance to be launched/started,
    // then uncomment the code below to wait a bit.
    //sleep(pthr->thread_num);

    // Note: stdout is going to be severely intermixed -- even on a single line so
    // would need a mechanism to serialize stdout (i.e. each thread completes its line).

    if (verbosity > 2) {
	cout << " Thread #" << pthr->thread_num << ": starts running on CPU #"
	     << pthr->cpu << endl;
    }

    pthr->thread_returned_value = pthr->run();

    // Note: if a thread calls pthread_exit(), it will NOT reach here!

    if (verbosity > 2) {
	cout << " Thread #" << pthr->thread_num << ": finishes running on CPU #"
	     << pthr->cpu << "; returning " << pthr->thread_returned_value << endl;
    }

    return pthr->thread_returned_value;
}


void
SimplePthread::launch_threads(const size_t num_threads)
{
    // A much simpler alternative is declaring SimplePthread threads[num_threads]
    // to keep threads[] on stack.  Then *NO* changes to the remaining codes!
    //SimplePthread threads[num_threads];
    std::vector<SimplePthread> threads(num_threads);

    if (verbosity > 1) {
	cout << "Creating/launching " << num_threads << " threads:" << endl;
    }

    for (auto &thr : threads) {
	// Assign each thread a unique small uint to distinguish
	thr.thread_num = (&thr - &threads[0]) + 1;
	if (verbosity > 3) {
	    cout << "  Thread #" << thr.thread_num << ": being created/launched" << endl;
	}
	pthread_create(thr.ptr_to_thread_id(), NULL, thread_entry, &thr);
    }

    if (verbosity > 1) {
	cout << "Waiting for " << num_threads << " threads to complete..." << endl;
    }

    for (auto &thr : threads) {
	void *result;

	pthread_join(*(thr.ptr_to_thread_id()), &result);
	if (verbosity > 3) {
	    cout << "  Thread #" << thr.thread_num << ": ran on CPU #" << thr.cpu
		 << ", returned " << result << endl;
	}
    }

    if (verbosity > 1) {
	cout << "All " << num_threads << " threads finished" << endl;
    }
}



#if !defined(SIMPLE_PTHREAD_EXTERNAL)

// This is the gut of what's going to be done within each thread
void *
SimplePthread::run()
{
    if (thread_num & 1) thread_terminate((void *) ((intptr_t) cpu));
    return (void *) ((intptr_t) cpu);
}

#endif


int
main(int argc, char *argv[])
{
    const size_t nthreads = (argc < 2) ? 8 : atoi(argv[1]);

    SimplePthread::launch_threads(nthreads);

    return 0;
}
