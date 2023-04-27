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


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.left = Node(12)
root.right.right = Node(20)

root.print_tree()

node = root.search(11)
if node:
    print(True)
else:
    print(False)

