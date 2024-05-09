#include "lists.h"

/**
 * check_cycle - a function to check the presence of a cycle in a singly
 * 	linked list
 * @list: pointer to the head of the list
 * Return: is to return 0 if no cycle, otherwise 1
 */

int check_cycle(listint_t *list)
{
	listint_t *p;
	char i = 0;

	if (list == NULL)
		return (0);
	p = list;
	while (list->next != NULL)
	{
		if (list->next == p)
			return (1);
		if (i == 4)
		{
			if (list->next == p)
				return (1);
			p = list->next;
			i = 0;
		}
		list = list->next;
		i++;
	}
	return (0);
}
