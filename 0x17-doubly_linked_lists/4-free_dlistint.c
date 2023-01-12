#include "lists.h"

/**
 * free_dlistint - free doubly linked list `head'
 * @head: pointer to head of list
 */
void free_dlistint(dlistint_t *head)
{
	if (head == NULL)
		return;
	while (head->next)
	{
		head = head->next;
		free(head->prev);
	}
	free(head);
}
