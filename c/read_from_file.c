#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int num = atoi(argv[1]);

  FILE *fd = fopen(argv[2], "r");
  int secrets[100];
  for (int i = 0; i < num; i++) {
    fscanf(fd, "%d\n", &secrets[i]);
    printf("i=%d, read=%d\n", i, secrets[i]);
  }
}
