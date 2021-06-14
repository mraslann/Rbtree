import rbtree as rb


def insert(t, z):
    z = rb.Node, x = rb.Node, y = rb.Node
    t = rb.Rbtree
    y = t.nil
    x = t.root
    while x != t.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == t.nil:
        t.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = t.nil
    z.right = t.nil
    z.colour = 1
    insertfixup(t, z)#


def insertfixup(self, k):
    while k.parent.color == 1:
        if k.parent == k.parent.parent.right:
            u = k.parent.parent.left
            if u.color == 1:
                u.color = 0
                k.parent.color = 0
                k.parent.parent.color = 1
                k = k.parent.parent
            else:
                if k == k.parent.left:
                    k = k.parent
                    self.right_rotate(k)
                k.parent.color = 0
                k.parent.parent.color = 1
                self.left_rotate(k.parent.parent)
        else:
            u = k.parent.parent.right

            if u.color == 1:
                u.color = 0
                k.parent.color = 0
                k.parent.parent.color = 1
                k = k.parent.parent
            else:
                if k == k.parent.right:
                    k = k.parent
                    self.left_rotate(k)
                k.parent.color = 0
                k.parent.parent.color = 1
                self.right_rotate(k.parent.parent)
        if k == self.root:
            break
    self.root.color = 0



