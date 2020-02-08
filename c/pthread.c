// To build:
//	make  LDLIBS=-lpthread  <this_file_no_suffix>
// Don't even need a Makefile!

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <pthread.h>
#include <errno.h>

#define handle_error_en(en, msg)			\
    do { errno = en; perror(msg); exit(EXIT_FAILURE); } while (0)

static void
display_pthread_attr(pthread_attr_t *attr, char *prefix)
{
    int s, i;
    size_t v;
    void *stkaddr;
    struct sched_param sp;

    s = pthread_attr_getdetachstate(attr, &i);
    if (s != 0)
	handle_error_en(s, "pthread_attr_getdetachstate");
    printf("%sDetach state        = %s\n", prefix,
	   (i == PTHREAD_CREATE_DETACHED) ? "PTHREAD_CREATE_DETACHED" :
	   (i == PTHREAD_CREATE_JOINABLE) ? "PTHREAD_CREATE_JOINABLE" :
	   "???");

    s = pthread_attr_getscope(attr, &i);
    if (s != 0)
	handle_error_en(s, "pthread_attr_getscope");
    printf("%sScope               = %s\n", prefix,
	   (i == PTHREAD_SCOPE_SYSTEM)  ? "PTHREAD_SCOPE_SYSTEM" :
	   (i == PTHREAD_SCOPE_PROCESS) ? "PTHREAD_SCOPE_PROCESS" :
	   "???");

    s = pthread_attr_getinheritsched(attr, &i);
    if (s != 0)
	handle_error_en(s, "pthread_attr_getinheritsched");
    printf("%sInherit scheduler   = %s\n", prefix,
	   (i == PTHREAD_INHERIT_SCHED)  ? "PTHREAD_INHERIT_SCHED" :
	   (i == PTHREAD_EXPLICIT_SCHED) ? "PTHREAD_EXPLICIT_SCHED" :
	   "???");

    s = pthread_attr_getschedpolicy(attr, &i);
    if (s != 0)
	handle_error_en(s, "pthread_attr_getschedpolicy");
    printf("%sScheduling policy   = %s\n", prefix,
	   (i == SCHED_OTHER) ? "SCHED_OTHER" :
	   (i == SCHED_FIFO)  ? "SCHED_FIFO" :
	   (i == SCHED_RR)    ? "SCHED_RR" :
	   "???");

    s = pthread_attr_getschedparam(attr, &sp);
    if (s != 0)
	handle_error_en(s, "pthread_attr_getschedparam");
    printf("%sScheduling priority = %d\n", prefix, sp.sched_priority);

    s = pthread_attr_getguardsize(attr, &v);
    if (s != 0)
	handle_error_en(s, "pthread_attr_getguardsize");
    printf("%sGuard size          = %d bytes\n", prefix, v);

    s = pthread_attr_getstack(attr, &stkaddr, &v);
    if (s != 0)
	handle_error_en(s, "pthread_attr_getstack");
    printf("%sStack address       = %p\n", prefix, stkaddr);
    printf("%sStack size          = 0x%x bytes\n", prefix, v);
}


static void *
thread_start(void *arg)
{
    const unsigned int thr_num = (unsigned int) ((intptr_t) arg);
    int s;
    pthread_attr_t gattr;

    /* pthread_getattr_np() is a non-standard GNU extension that
       retrieves the attributes of the thread specified in its
       first argument */

    s = pthread_getattr_np(pthread_self(), &gattr);
    if (s != 0)
	handle_error_en(s, "pthread_getattr_np");

    // Should acquire a lock here so display won't intermixed
    printf("\n\nThread #%2u: now running on CPU #%2u\n", thr_num, sched_getcpu());

    printf("Thread #%2u attributes:\n", thr_num);
    display_pthread_attr(&gattr, "\t");
    // End of lock

    pthread_exit((void *) ((intptr_t) sched_getcpu()));
}


static void
launch_threads(const size_t nthreads)
{
    pthread_t thread_array[nthreads + 1];
    //pthread_attr_t attr;
    unsigned int i;

    for (i = 1; i <= nthreads; i++)
    {
        //pthread_attr_init(&attr);
        pthread_create(&thread_array[i], NULL, thread_start,
                       (void *) ((intptr_t) i));
        //pthread_attr_destroy(&attr);
    }

    for (i = 1; i <= nthreads; i++)
    {
        void *result;

        pthread_join(thread_array[i], &result);
        printf("Thread #%2u reported it ran on CPU #%2u\n",
               i, (unsigned int) ((intptr_t) result));
    }
}


int
main(int argc, char *argv[])
{
    const size_t nthreads = (argc < 2) ? 10 : atoi(argv[1]);

    printf("Launching %u threads:\n", nthreads);

    launch_threads(nthreads);

    return 0;
}
