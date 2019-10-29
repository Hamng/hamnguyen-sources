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
//#include <vector>
#include <thread>
#include <sched.h>
//#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

using namespace std;


static unsigned int verbosity = 4;


class MyThreadObj {
  public:
    void operator()();
    MyThreadObj(const unsigned int thr_no): thread_num(thr_no) {}

  protected:
    const unsigned int	thread_num;	// a small unique uint to distinguish threads
    unsigned int	cpu;		// the CPU# a thread runs on
};


void MyThreadObj::operator()()
{
    cpu = sched_getcpu();
    if (verbosity > 2) {
	cout << " Thread #" << thread_num << ": starts running on CPU #"
	     << cpu << endl;
    }
}


void
launch_threads(const size_t num_threads)
{
    std::thread *threads[num_threads];
    unsigned int i;

    if (verbosity > 1) {
	cout << "Creating/launching " << num_threads << " threads:" << endl;
    }

    for (i = 0; i < num_threads; i++) {
	if (verbosity > 3) {
	    cout << "  Thread #" << i + 1 << ": being created/launched" << endl;
	}
	threads[i] = new std::thread(
*(new MyThreatObj(i + 1))
);
    }

    if (verbosity > 1) {
	cout << "Waiting for " << num_threads << " threads to complete..." << endl;
    }

    for (i = 0; i < num_threads; i++) {
	threads[i]->join();

	if (verbosity > 3) {
	    cout << "  Thread #" << i + 1 << ": joined" << endl;
	}
    }

    if (verbosity > 1) {
	cout << "All " << num_threads << " threads finished" << endl;
    }
}


int
main(int argc, char *argv[])
{
    const size_t nthreads = (argc < 2) ? 8 : atoi(argv[1]);

    launch_threads(nthreads);

    return 0;
}
