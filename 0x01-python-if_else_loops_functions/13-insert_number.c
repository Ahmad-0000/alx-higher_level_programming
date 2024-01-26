#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - is a function to insert a node in a sorted doubly linked list
 *	based on the value of the numbers
 * @head: is a pointer to a pointer to the first node in the list
 * @number: is a number to be inserted in the node
 *
 * Return: is to return the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_ptr, *tmp;

	if (head == NULL || *head == NULL)
		return (NULL);
	tmp = *head;
	node_ptr = malloc(sizeof(listint_t));
	if (node_ptr == NULL)
		return (NULL);
	node_ptr->n = number;
	while (tmp->next != NULL && tmp->next->n < number)
		tmp = tmp->next;
	node_ptr->next = tmp->next;
	tmp->next = node_ptr;
	return (node_ptr);
}
