#include <stdio.h>
#include <string>

int
main(int argc, char *argv[])
{
	std::string fname = __func__;
	std::string msg = "what to say";
	printf("%s(): msg='%s'\n", fname.c_str(), msg.c_str());
}
