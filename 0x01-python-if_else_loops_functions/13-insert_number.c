#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_ptr = malloc(sizeof(listint_t));

	if (node_ptr == NULL)
		return NULL;
	node_ptr->next = NULL;
	node_ptr->n = number;
	while ((*head)->next != NULL)
	{
		*head = (*head)->next;
	}
	(*head)->next = node_ptr;
	return (node_ptr);
}
