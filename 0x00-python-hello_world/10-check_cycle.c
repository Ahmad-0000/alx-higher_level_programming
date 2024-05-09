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

	if (list == NULL)
		return (0);
	p = list;
	while (list->next != NULL)
	{
		if (list->next == p)
			break;
		list = list->next;
	}
	if (list->next == p)
		return (1);
	return (0);
}
