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

# node = root.search(11)
# if node:
#     print(True)
# else:
#     print(False)

class LeftLeaningRedBlackTree:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.color = "RED"

    def __init__(self):
        self.root = None

    def add(self, key, value):
        self.root = self._add(self.root, key, value)
        self.root.color = "BLACK"

    def _add(self, node, key, value):
        # Если узел пустой, создаем новый узел с заданным ключом и значением
        if node is None:
            return self.Node(key, value)

        # Если ключ меньше, чем ключ текущего узла, рекурсивно добавляем элемент в левое поддерево
        if key < node.key:
            node.left = self._add(node.left, key, value)

        # Если ключ больше, чем ключ текущего узла, рекурсивно добавляем элемент в правое поддерево
        elif key > node.key:
            node.right = self._add(node.right, key, value)

        # Проверяем баланс и перебалансируем дерево, если необходимо
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        return node

    def _is_red(self, node):
        # Проверяем, является ли цвет узла красным
        if node is None:
            return False
        return node.color == "RED"

    def _rotate_left(self, node):
        # Выполняем левый поворот
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = "RED"
        print(f"Выполняем левый поворот узла {node.key}")
        self._print_tree()
        return x

    def _rotate_right(self, node):
        # Выполняем правый поворот
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = "RED"
        print(f"Выполняем правый поворот узла {node.key}")
        self._print_tree()
        return x

    def _flip_colors(self, node):
        # Меняем цвета узлов
        node.color = "RED"
        node.left.color = "BLACK"
        node.right.color = "BLACK"
        print(f"Меняем цвета узлов для узла {node.key}")
        self._print_tree()

    def _print_tree(self):
    # Рекурсивно выводим дерево в консоль
        def traverse(node, level=0):
            if node is not None:
                traverse(node.left, level + 1)
                print(f"Level {level}: {node.key} ({node.color})")
                traverse(node.right, level + 1)

        print("\n")
        traverse(self.root)