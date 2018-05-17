#include "holberton.h"

unsigned int binary_to_uint(const char *b)
{
	int i = 0;
	unsigned int sum;
	unsigned int power;

	if (b == NULL)
		return (0);
	while (b[i] != '\0')
	{
		if (b[i] != '0' && b[i] != '1')
			return (0);
		i++;
	}
	i--; /** Account for NULL byte */
	sum = 0;
	power = 1;
	while (i >= 0)
	{
		if (b[i] == '1')
			sum += power;
		power *= 2;
		i--;
	}
	return (sum);
}
