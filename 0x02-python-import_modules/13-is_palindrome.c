#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - A function to check if a singly linked list if 
 * 	a linked list is palindrome
 * @head: a pointer to pointer to the 1st node
 * Return: is to return 1 if true, else 0
 *
 **/

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int length = 0, last, half;
	int *numbers;

	if (!head)
		return 0;
	if (*head == NULL)
		return 1;
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		length++;
	}
	numbers = malloc(sizeof(*numbers) * length);
	if (!numbers)
		return 0;
	length = 0;
	temp = *head;
	while (temp)
	{
		numbers[length] = temp->n;
		temp = temp->next;
		length++;
	}
	last = length - 1;
	length = 0;
	half = last / 2;
	while (last >= half)
	{
		if (numbers[length] != numbers[last])
			return 0;
		last--;
		length++;
	}
	return 1;
}
