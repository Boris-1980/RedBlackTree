# class Node:

#     def __init__(self, data, parent=None):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.parent = parent
#         self.color = 1

#     def search(self, val):
#         if self.data == val:
#             return self
#         if self.data > val:
#             return self.left.search(val) if self.left else None
#         else:
#             return self.right.search(val) if self.right else None

#     def print_tree(self):
#         if self.left:
#             self.left.print_tree()
#         print(self.data)
#         if self.right:
#             self.right.print_tree()


# root = Node(10)
# root.left = Node(5)
# root.right = Node(15)
# root.left.left = Node(3)
# root.left.right = Node(8)
# root.right.left = Node(12)
# root.right.right = Node(20)

# root.print_tree()

class Node: 

    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.color = 1

    def search(self, val):
        if self.data == val:
            return self
        if self.data > val:
            return self.left.search(val) if self.left else None
        else:
            return self.right.search(val) if self.right else None

    def print_tree(self):
            if self.left:
            self.left.print_tree()
            print(self.data)
            if self.right:
            self.right.print_tree()
    
    def insert(self, data):
    new_node = Node(data)

    # Perform BST insertion
    if self.root is None:
        # Case 1: Empty tree
        self.root = new_node
        self.root.color = Node.BLACK
        return
    else:
        # Find the insertion point
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        # Insert the new node
        new_node.parent = parent
        if new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

    # Fix the tree
    self.fix_insert(new_node)


    def fix_violation(self):
    while self.parent and self.parent.color == 1:
        if self.parent == self.parent.parent.left:
            uncle = self.parent.parent.right

            if uncle and uncle.color == 1:
                self.parent.color = 0
                uncle.color = 0
                self.parent.parent.color = 1
                self = self.parent.parent
            else:
                if self == self.parent.right:
                    self = self.parent
                    self.left_rotate()
                self.parent.color = 0
                self.parent.parent.color = 1
                self.parent.parent.right_rotate()
        else:
            uncle = self.parent.parent.left

            if uncle and uncle.color == 1:
                self.parent.color = 0
                uncle.color = 0
                self.parent.parent.color = 1
                self = self.parent.parent
            else:
                if self == self.parent.left:
                    self = self.parent
                    self.right_rotate()
                self.parent.color = 0
                self.parent.parent.color = 1
                self.parent.parent.left_rotate()

    self.color = 0
    while self.parent:
        self = self.parent

        def left_rotate(self):
            new_root = self.right
            self.right = new_root.left
            if new_root.left:
                new_root.left.parent = self
                new_root.parent = self.parent
            if not self.parent:
                root = new_root
            elif self == self.parent.left:
                self.parent.left = new_root
            else:
                self.parent.right = new_root
                new_root.left = self
                self.parent = new_root


    def fix_insert(self, node):
    while node.parent is not None and node.parent.color == RED:
        if node.parent == node.parent.parent.left:
            uncle = node.parent.parent.right
            if uncle is not None and uncle.color == RED:
                # Case 1: Parent and uncle are both red
                node.parent.color = BLACK
                uncle.color = BLACK
                node.parent.parent.color = RED
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    # Case 2: Parent is red and uncle is black, and node is a right child
                    node = node.parent
                    self.rotate_left(node)
                # Case 3: Parent is red and uncle is black, and node is a left child
                node.parent.color = BLACK
                node.parent.parent.color = RED
                self.rotate_right(node.parent.parent)
        else:
            uncle = node.parent.parent.left
            if uncle is not None and uncle.color == RED:
                # Case 4: Parent and uncle are both red, and node is a right child
                node.parent.color = BLACK
                uncle.color = BLACK
                node.parent.parent.color = RED
                node = node.parent.parent
            else:
                if node == node.parent.left:
                    # Case 5: Parent is red and uncle is black, and node is a left child
                    node = node.parent
                    self.rotate_right(node)
                # Case 6: Parent is red and uncle is black, and node is a right child
                node.parent.color = BLACK
                node.parent.parent.color = RED
                self.rotate_left(node.parent.parent)
    self.root.color = BLACK

def right_rotate(self):
    new_root = self.left
    self.left = new_root.right
    if new_root.right:
        new_root.right.parent = self
        new_root.parent = self.parent
    if not self.parent:
        root = new_root
    elif self == self.parent.right:
        self.parent.right = new_root
    else:
        self.parent.left = new_root
        new_root.right = self
        self.parent = new_root

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.left = Node(12)
root.right.right = Node(20)

root.print_tree()

root.insert(9)
root.insert(7)
root.insert(13)
root.insert(18)

root.print_tree()


    