from insertion import insertfixup


class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class Rbtree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def insert(self, key):
        node = Node(key)
        node.left = self.TNULL
        node.right = self.TNULL

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            elif node.item > x.item:
                x = x.right
            else:

                return 2

        node.parent = y
        if y is None:          #node is first element
            self.root = node
        elif node.item < y.item:
            y.left = node
        elif node.item > y.item:
            y.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        insertfixup(self, node)

    def search_tree(self, node, key):
        if node == self.TNULL or key == node.item:
            return node

        if key < node.item:
            return self.search_tree(node.left, key)
        return self.search_tree(node.right, key)

    def search(self, k):
        node = self.search_tree(self.root, k)
        if node.item == k:
            print("Node was found")
            print(node.item)
        else:
            print("Node was not found")
        return

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def treeheight(self, node):
        if node is None:
            return -1
        else:
            return max(self.treeheight(node.left), self.treeheight(node.right)) + 1
