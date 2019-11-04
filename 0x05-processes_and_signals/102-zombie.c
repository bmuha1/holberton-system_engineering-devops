#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - Infinite loop
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Create 5 zombie processes
 *
 * Return: Always 0
 */
int main(void)
{
	pid_t child1 = fork();
	pid_t child2 = fork();
	pid_t child3 = fork();
	pid_t child4 = fork();
	pid_t child5 = fork();

	if (child1 > 0 && child2 > 0 && child3 > 0 && child4 > 0 &&
	    child5 > 0)
	{
		printf("Zombie process created, PID: %d\n", child1);
		printf("Zombie process created, PID: %d\n", child2);
		printf("Zombie process created, PID: %d\n", child3);
		printf("Zombie process created, PID: %d\n", child4);
		printf("Zombie process created, PID: %d\n", child5);
		infinite_while();
	}
	else
		exit(0);

	return (0);
}
