#include "binary_trees.h"
/**
 * binary_tree_insert_right - fxn inserts a node as the right-child of another
 * @parent: pointer to the node to insert right-child in
 * @value: value to store in the new node
 * Return: fxn returns pointer to new node or NULL if fails
 */

binary_tree_t *binary_tree_insert_right(binary_tree_t *parent, int value)
{
	binary_tree_t *new_node;

	if (parent == NULL)
		return (NULL);
	new_node = malloc(sizeof(binary_tree_t));
	if (new_node == NULL)
		return (NULL);
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->n = value;
	if (parent->right != NULL)
	{
		new_node->right = parent->right;
		parent->right = new_node;
		new_node->parent = parent;
		new_node->right->parent = new_node;
	}
	else
	{
		parent->right = new_node;
		new_node->parent = parent;
	}
	return (new_node);
}
