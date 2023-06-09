### Код с семинара

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

################################################################################

class Node: # Класс для узлов красно-черного дерева

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = "RED"  # Каждый новый узел при добавлении помечается красным


class RedBlackTree: # Класс для красно-черного дерева
  
    def __init__(self):
        self.nil = Node(None)  # Специальный узел-заглушка
        self.nil.color = "BLACK"
        self.root = self.nil

    def insert(self, key): # Вставка нового узла в дерево
    
        new_node = Node(key)
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = "RED"
        self.__insert_fixup(new_node)

    def __insert_fixup(self, node):# Восстановление свойств красно-черного дерева после вставки нового узла
 
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.__right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.__left_rotate(node.parent.parent)
        self.root.color = "BLACK"

    def __left_rotate(self, node): # Осуществляет левый поворот вокруг заданного узла
 
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

        
tree = RedBlackTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(9)
tree.insert(6)
tree.insert(8)
tree.insert(10)

current_node = tree.root
print("Дерево:")
print(current_node.key, current_node.color)
while current_node.left != tree.nil:
    current_node = current_node.left
    print(current_node.key, current_node.color)

current_node = tree.root
while current_node.right != tree.nil:
    current_node = current_node.right
    print(current_node.key, current_node.color)




#######################################################################################################################
#### Это пока усложненный код который не работает 

# class RedBlackNode:
#     def __init__(self, key, color='RED'):
#         self.key = key
#         self.color = color
#         self.left = None
#         self.right = None
#         self.parent = None

# class RedBlackTree:
#     def __init__(self):
#         self.nil = Node(0)
#         self.nil.color = 'BLACK'
#         self.root = self.nil


#     def insert(self, key):

#         new_node = Node(key)
#         new_node.left = self.nil
#         new_node.right = self.nil
#         new_node.color = 'RED'

#         parent = None
#         current = self.root

#     # Ищем место для вставки нового узла
#     while current != self.nil:
#         parent = current
#         if new_node.key < current.key:
#             current = current.left
#         else:
#             current = current.right

#     # Вставляем новый узел на место найденного листа
#     new_node.parent = parent
#     if parent == None:
#         self.root = new_node
#         new_node.color = 'BLACK'  # Новый узел является корнем дерева, устанавливаем его цвет в черный
#     elif new_node.key < parent.key:
#         parent.left = new_node
#     else:
#         parent.right = new_node

#     # Фиксируем изменения в дереве
#     self.__fix_insert(new_node)


#     def __fix_insert(self, new_node):
#         """
#         Балансирует красно-черное дерево после вставки нового узла
#         """
#         while new_node.parent.color == 'RED':
#             if new_node.parent == new_node.parent.parent.left:
#                 # Родитель находится на левой ветке
#                 y = new_node.parent.parent.right
#                 if y.color == 'RED':
#                     # Случай 1: дядя нового узла - красный
#                     new_node.parent.color = 'BLACK'
#                     y.color = 'BLACK'
#                     new_node.parent.parent.color = 'RED'
#                     new_node = new_node.parent.parent
#                 else:
#                     if new_node == new_node.parent.right:
#                         # Случай 2: новый узел - правый потомок
#                         new_node = new_node.parent
#                         self.__left_rotate(new_node)
#                     # Случай 3: новый узел - левый потомок
#                     new_node.parent.color = 'BLACK'
#                     new_node.parent.parent.color = 'RED'
#                     self.__right_rotate(new_node.parent.parent)
#             else:
#                 # Родитель находится на правой ветке
#                 y = new_node.parent.parent.left
#                 if y.color == 'RED':
#                     # Случай 1: дядя нового узла - красный
#                     new_node.parent.color = 'BLACK'
#                     y.color = 'BLACK'
#                     new_node.parent.parent.color = 'RED'
#                     new_node = new_node.parent.parent
#                 else:
#                     if new_node == new_node.parent.left:
#                         # Случай 2: новый узел - левый потомок
#                         new_node = new_node.parent
#                         self.__right_rotate(new_node)
#                     # Случай 3: новый узел - правый потомок
#                     new_node.parent.color = 'BLACK'
#                     new_node.parent.parent.color = 'RED'
#                     self.__left_rotate(new_node.parent.parent)

#         # Корень всегда должен быть черным
#         self.root.color = 'BLACK'

#     def delete(self, key):
#         """
#         Удаляет узел с заданным ключом из красно-черного дерева
#         """
#         # Ищем узел для удаления
#         current = self.root
#         while current != self.nil and current.key != key:
#             if key < current.key:
#                 current = current.left
#             else:
#                 current = current.right

#         # Узел не найден
#         if current == self.nil:
#             return

#         # Если удаляемый узел имеет не более одного потомка, просто заменяем его на потомка
#         if current.left == self.nil or current.right == self.nil:
#             child = current.left if current.left != self.nil else current.right
#             if current.parent == None:
#                 self.root = child
#             elif current == current.parent.left:
#                 current.parent.left = child
#             else:
#                 current.parent.right = child
#             child.parent = current.parent

#             # Если удаляемый узел был черным, возможно, нарушается баланс дерева
#             if current.color == 'BLACK':
#                 self.__fix_delete(child)
#         else:
#             # Удаляемый узел имеет двух потомков, находим его преемника и заменяем им удаляемый узел
#             successor = self.__tree_minimum(current.right)
#             current.key = successor.key
#             self.delete(successor)

#     def __fix_delete(self, node):
#         """
#         Балансирует красно-черное дерево после удаления узла
#         """
#         while node != self.root and node.color == 'BLACK':
#             if node == node.parent.left:
#                 # Узел находится на левой ветке
#                 sibling = node.parent.right
#                 if sibling.color == 'RED':
#                     # Случай 1: брат узла - красный
#                     sibling.color = 'BLACK'
#                     node.parent.color = 'RED'
#                     self.__left_rotate(node.parent)
#                     sibling = node.parent.right
#                 if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
#                     # Случай 2: оба потомка брата - черные
#                     sibling.color = 'RED'
#                     node = node.parent
#                 else:
#                     if sibling.right.color == 'BLACK':
#                         # Случай 3: левый потомок брата - красный, правый - черный
#                         sibling.left.color = 'BLACK'
#                         sibling.color = 'RED'
#                         self.__right_rotate(sibling)
#                         sibling = node.parent.right
#                     # Случай 4: правый потомок брата - красный
#                     sibling.color = node.parent.color
#                     node.parent.color = 'BLACK'
#                     sibling.right.color = 'BLACK'
#                     self.__left_rotate(node.parent)
#                     node = self.root.right
#             else:
#                 # Узел находится на правой ветке
#                 sibling = node.parent.left
#                 if sibling.color == 'RED':
#                     # Случай 1: брат узла - красный
#                     sibling.color = 'BLACK'
#                     node.parent.color = 'RED'
#                     self.__right_rotate(node.parent)
#                     sibling = node.parent.left
#                 if sibling.left.color == 'BLACK' and sibling.right.color == 'BLACK':
#                     # Случай 2: оба потомка брата - черные
#                     sibling.color = 'RED'
#                     node = node.parent
#                 else:
#                     if sibling.left.color == 'BLACK':
#                         # Случай 3: правый потомок брата - красный, левый - черный
#                         sibling.right.color = 'BLACK'
#                         sibling.color = 'RED'
#                         self.__left_rotate(sibling)
#                         sibling
#                         sibling = node.parent.left
#                     # Случай 4: левый потомок брата - красный
#                     sibling.color = node.parent.color
#                     node.parent.color = 'BLACK'
#                     sibling.left.color = 'BLACK'
#                     self.__right_rotate(node.parent)
#                     node = self.root.left

#         node.color = 'BLACK'

#     def __tree_minimum(self, node):
#         """
#         Находит узел с минимальным значением ключа в поддереве, корнем которого является заданный узел
#         """
#         while node.left != self.nil:
#             node = node.left
#         return node

#     def __left_rotate(self, node):
#         """
#         Осуществляет левый поворот вокруг заданного узла
#         """
#         right_child = node.right
#         node.right = right_child.left
#         if right_child.left != self.nil:
#             right_child.left.parent = node
#         right_child.parent = node.parent
#         if node.parent == None:
#             self.root = right_child
#         elif node == node.parent.left:
#             node.parent.left = right_child
#         else:
#             node.parent.right = right_child
#         right_child.left = node
#         node.parent = right_child

#     def __right_rotate(self, node):
#         """
#         Осуществляет правый поворот вокруг заданного узла
#         """
#         left_child = node.left
#         node.left = left_child.right
#         if left_child.right != self.nil:
#             left_child.right.parent = node
#         left_child.parent = node.parent
#         if node.parent == None:
#             self.root = left_child
#         elif node == node.parent.right:
#             node.parent.right = left_child
#         else:
#             node.parent.left = left_child
#         left_child.right = node
#         node.parent = left_child

# rbt = RedBlackTree()

# # Вставляем элементы в дерево
# rbt.insert(10)
# rbt.insert(20)
# rbt.insert(30)
# rbt.insert(100)
# rbt.insert(90)
# rbt.insert(40)

# # Печатаем элементы дерева в отсортированном порядке
# print("Элементы дерева в отсортированном порядке: ", end="")
# rbt.inorder_traversal(rbt.root)
# print()

# # Удаляем элементы из дерева
# rbt.delete(10)
# rbt.delete(20)

# # Печатаем элементы дерева в отсортированном порядке
# print("Элементы дерева в отсортированном порядке: ", end="")
# rbt.inorder_traversal(rbt.root)
# print()

    