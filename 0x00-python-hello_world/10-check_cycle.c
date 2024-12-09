#include "lists.h"

/**
 * check_cycle - a function to check the presence of a cycle in a singly
 * 	linked list
 * @list: pointer to the head of the list
 * Return: is to return 0 if no cycle, otherwise 1
 */

int check_cycle(listint_t *list)
{
	listint_t *loopptr;
	int i = 0;

	if (!list)
		return (0);
	loopptr = list;
	while (list->next != NULL)
	{
		if (list->next == loopptr)
			return (1);
		if (i == 10)
		{
			loopptr = loopptr->next->next->next->next->next;
			i = 0;
		}
		list = list->next;
		i++;
	}
	return (0);
}
