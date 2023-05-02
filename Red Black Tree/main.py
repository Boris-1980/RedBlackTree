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
    
    def insert(self, val):
        if self.data == val:
        return
        if self.data > val:
            if self.left:
            self.left.insert(val)
            else:
            self.left = Node(val, self)
            else:
                if self.right:
            self.right.insert(val)
        else:
            self.right = Node(val, self)
        self.fix_violation()

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


    