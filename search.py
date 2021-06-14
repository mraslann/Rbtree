import rbtree


def search(tree, node, key):
    if node == tree.nil or key == node.key:
        return node

    if key < node.item:
        return search(tree, node.left, key)
    return search(tree, node.right, key)
