#include <stdio.h>
#include <sched.h>
#include <numa.h>

int
main(int argc, char *argv[])
{
  const int cpu  = sched_getcpu();
  const int node = numa_available() < 0 ? -125 : numa_node_of_cpu(cpu);

  printf("sched_getcpu() returned %d; numa_node_of_cpu() returned %d\n",
         cpu, node);

  return 0;
}
