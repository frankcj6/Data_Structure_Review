#       different with binary tree( sorted according to value)
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.auto_insert(data, self.root)

    def auto_insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self.auto_insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self.auto_insert(data, cur_node.right)
        else:
            print('Value is already in the BST.')

    def Find(self, data):
        if self.root:
            is_found = self.auto_find(data, self.root)
            if is_found is True:
                return True
            return False
        return False

    def auto_find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self.auto_find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self.auto_find(data, cur_node.left)
        if data == cur_node.data:
            return True


#  checking the BST property
    def inorder_print_tree(self):
        if self.root:
            self.inorder_print(self.root)


    def inorder_print(self, cur_node):
        if cur_node:
            self.inorder_print(cur_node.left)
            print(str(cur_node.data))
            self.inorder_print(cur_node.right)

    def is_BST(self):
        if self.root:
            is_satisfied = self.auto_is_bst(self.root, self.root.data)

            if is_satisfied is None:
                return True
            return False
        return True

    def auto_is_bst(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.data:
                return self.auto_is_bst(cur_node.left, cur_node.left.data)
            return False
        if cur_node.right:
            if data < cur_node.right.data:
                return self.auto_is_bst(cur_node.right, cur_node.right.data)
            return False


#  time complexity
#  space  o(n)
#  search o(log n)
#  insert o(log n)
#  delete o(log n)


#  generate tree
BST = BinarySearchTree()
BST.insert(4)
BST.insert(2)
BST.insert(5)
BST.insert(8)
BST.insert(10)

print(BST.Find(5))

BST.inorder_print(BST.root)

tree = BinarySearchTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

tree.inorder_print(tree.root)

print(BST.is_BST())
print(tree.is_BST())