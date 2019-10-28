

#ifndef _SIMPLE_PTHREAD_HH


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


#endif		/* simple_pthread.hh */
