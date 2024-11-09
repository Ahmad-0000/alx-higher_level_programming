#include <stdlib.h>
#include "lists.h"


/**
 * insert_node - is a function to insert a node in a sorted doubly linked list
 *	based on the value of the numbers
 * @head: is a pointer to a pointer to the first node in the list
 * @number: is a number to be inserted in the node
 *
 * Return: is to return the address of the new node or Null in failure
 **/


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(*node));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
		return node;
	}
	tmp = *head;
	if (tmp->next == NULL) 
	{
		if (node->n > (*head)->n)
		{
			(*head)->next = node;
		}
		else
		{
			node->next = *head;
			*head = node;
		}
		return node;
	}
	while (tmp->next != NULL && tmp->next->n < number)
		tmp = tmp->next;
	if (!tmp->next)
	{
		tmp->next = node;
		return node;
	}
	node->next = tmp->next;
	tmp->next = node;
	return (node);
}
