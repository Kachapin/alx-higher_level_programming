#include "lists.h"
int is_palindrome(listint_t **head)
{
	int *ptr, i = 0, j;
	listint_t *current;

	current = *head;
	while (current)
	{
		i++;
		current = current->next;
	}
	ptr = malloc(sizeof(int) * i);

	current = *head;
	for (j = 0; j < i; j++)
	{
		ptr[j] = current->n;
		current = current->next;
	}
	current = *head;
	i--;
	while(current)
	{
		if (current->n != ptr[i])
		{
			free(ptr);
			return (0);
		}
		i--;
		current = current->next;
	}
	free(ptr);
	return 1;
}
