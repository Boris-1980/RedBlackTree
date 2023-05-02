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

class RedBlackNode:

    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.nil = RedBlackNode(None, 'BLACK')
        self.root = self.nil

    def insert(self, key):
        """
        Вставляет новый узел в красно-черное дерево с заданным ключом
        """
        # Создаем новый узел
        new_node = RedBlackNode(key)

        # Устанавливаем его потомком равным nil
        new_node.left = self.nil
        new_node.right = self.nil

        # Устанавливаем корень как родитель нового узла
        new_node.parent = self.root
        # Ищем место для вставки нового узла
        current = self.root
        parent = None
        while current != self.nil:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        # Устанавливаем родителя нового узла
        new_node.parent = parent

        # Вставляем новый узел в дерево
        if parent == None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Балансируем дерево
        self.__fix_insert(new_node)

    def __fix_insert(self, new_node):
        """
        Балансирует красно-черное дерево после вставки нового узла
        """
        while new_node.parent.color == 'RED':
            if new_node.parent == new_node.parent.parent.left:
                # Родитель находится на левой ветке
                y = new_node.parent.parent.right
                if y.color == 'RED':
                    # Случай 1: дядя нового узла - красный
                    new_node.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    new_node.parent.parent.color = 'RED'
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        # Случай 2: новый узел - правый потомок
                        new_node = new_node.parent
                        self.__left_rotate(new_node)
                    # Случай 3: новый узел - левый потомок
                    new_node.parent.color = 'BLACK'
                    new_node.parent.parent.color = 'RED'
                    self.__right_rotate(new_node.parent.parent)
            else:
                # Родитель находится на правой ветке
                y = new_node.parent.parent.left
                if y.color == 'RED':
                    # Случай 1: дядя нового узла - красный
                    new_node.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    new_node.parent.parent.color = 'RED'
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        # Случай 2: новый узел - левый потомок
                        new_node = new_node.parent
                        self.__right_rotate(new_node)
                    # Случай 3: новый узел - правый потомок
                    new_node.parent.color = 'BLACK'
                    new_node.parent.parent.color = 'RED'
                    self.__left_rotate(new_node.parent.parent)

        # Корень всегда должен быть черным
        self.root.color = 'BLACK'

    def delete(self, key):
        """
        Удаляет узел с заданным ключом из красно-черного дерева
        """
        # Ищем узел для удаления
        current = self.root
        while current != self.nil and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right

        # Узел не найден
        if current == self.nil:
            return

        # Если удаляемый узел имеет не более одного потомка, просто заменяем его на потомка
        if current.left == self.nil or current.right == self.nil:
            child = current.left if current.left != self.nil else current.right
            if current.parent == None:
                self.root = child
            elif current == current.parent.left:
                current.parent.left = child
            else:
                current.parent.right = child
            child.parent = current.parent

            # Если удаляемый узел был черным, возможно, нарушается баланс дерева
            if current.color == 'BLACK':
                self.__fix_delete(child)
        else:
            # Удаляемый узел имеет двух потомков, находим его преемника и заменяем им удаляемый узел
            successor = self.__tree_minimum(current.right)
            current.key = successor.key
            self.delete(successor)

    def __fix_delete(self, node):
        """
        Балансирует красно-черное дерево после удаления узла
        """
        while node != self.root and node.color == 'BLACK':
            if node == node.parent.left:
                # Узел находится на левой ветке
                sibling = node.parent.right
                if sibling.color == 'RED':
                    # Случай 1: брат узла - красный
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.__left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    # Случай 2: оба потомка брата - черные
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.right.color == 'BLACK':
                        # Случай 3: левый потомок брата - красный, правый - черный
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self.__right_rotate(sibling)
                        sibling = node.parent.right
                    # Случай 4: правый потомок брата - красный
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self.__left_rotate(node.parent)
                    node = self.root.right
            else:
                # Узел находится на правой ветке
                sibling = node.parent.left
                if sibling.color == 'RED':
                    # Случай 1: брат узла - красный
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.__right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
                    # Случай 2: оба потомка брата - черные
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.left.color == 'BLACK':
                        # Случай 3: правый потомок брата - красный, левый - черный
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self.__left_rotate(sibling)
                        sibling
                        sibling = node.parent.left
                    # Случай 4: левый потомок брата - красный
                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self.__right_rotate(node.parent)
                    node = self.root.left

        node.color = 'BLACK'

    def __tree_minimum(self, node):
        """
        Находит узел с минимальным значением ключа в поддереве, корнем которого является заданный узел
        """
        while node.left != self.nil:
            node = node.left
        return node

    def __left_rotate(self, node):
        """
        Осуществляет левый поворот вокруг заданного узла
        """
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.nil:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent == None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def __right_rotate(self, node):
        """
        Осуществляет правый поворот вокруг заданного узла
        """
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.nil:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent == None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

rbt = RedBlackTree()

# Вставляем элементы в дерево
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(100)
rbt.insert(90)
rbt.insert(40)

# Печатаем элементы дерева в отсортированном порядке
print("Элементы дерева в отсортированном порядке: ", end="")
rbt.inorder_traversal(rbt.root)
print()

# Удаляем элементы из дерева
rbt.delete(10)
rbt.delete(20)

# Печатаем элементы дерева в отсортированном порядке
print("Элементы дерева в отсортированном порядке: ", end="")
rbt.inorder_traversal(rbt.root)
print()


    