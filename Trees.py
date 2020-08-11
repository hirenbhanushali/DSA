# defining a class Node for Tree Data Structure
# still not sure if we need getter and setter functions


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def get_left(self, node):
        if self.left != None:
            return self.left

    def get_right(self, node):
        if self.right != None:
            return self.right


# defining a class Tree which has attribute root
class Tree:

    def __init__(self, node=None):
        self.root = node

    def get_root(self):
        return self.root.value


n1 = Node(5)
n2 = Node(4)
n3 = Node(7)
n4 = Node(2)
n5 = Node(6)


x = Tree(n1)

x.root.left = n2
x.root.right = n3
x.root.left.left = n4
x.root.left.right = n5

# implementing inorder traversal


def inorder_traversal(root):
    if root != None:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)

# implementing preorder traversal


def preorder_traversal(root):
    if root != None:
        print(root.value)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# implementing postorder traversal


def postorder_traversal(root):
    if root != None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value)

print("Inorder Traversal:")
inorder_traversal(x.root)
print("Preorder Traversal")
preorder_traversal(x.root)
print("Postorder Traversal")
postorder_traversal(x.root)

# size of a tree


def size_of_tree(root):
    if root == None:
        return 0
    return 1 + size_of_tree(root.left) + size_of_tree(root.right)

j = size_of_tree(x.root)
print("Size of Tree:", j)

#Maximum in Tree


def max_in_tree(root):
    if root == None:
        return 0
    return max(root.value, max(max_in_tree(root.left), max_in_tree(root.right)))

m = max_in_tree(x.root)
print("Maximum:", m)

# Height of the Tree


def height_of_tree(root):
    if root == None:
        return 0
    return max(height_of_tree(root.left), height_of_tree(root.right)) + 1

h = height_of_tree(x.root)
print("Height of Tree:", h)
