#include <stdlib.h>
#include <stdio.h>
/**
 *
 *
 *
 */
int infinite_while(void)
{
	int pid;

	pid = fork();
	if (pid != 0)
	{
		while (1)
		{
			sleep(1);
		}
	}
	return (0);
}
