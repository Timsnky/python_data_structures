"""
Insert Data
Remove Data
Search Data
"""

class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def get_max_value(self):
        if self.root:
            node = self.get_max(self.root)
            return node.data

    def get_max(self, node):
        if node.right_child:
            return self.get_max(node.right_child)

        return node

    def get_min_value(self):
        if self.root:
            node = self.get_min(self.root)
            return node.data

    def get_min(self, node):
        if node.left_child:
            return self.get_min(node.left_child)

    def in_order_traverse(self):
        if self.root:
            return self.in_order_traverse_node(self.root)

    def in_order_traverse_node(self, node):
        if node.left_child:
            self.in_order_traverse_node(node.left_child)

        print(str(node.data) + " ")

        if node.right_child:
            self.in_order_traverse_node(node.right_child)

    def insert(self, data):
        self.root = self.insert_node(self.root, data)

    def insert_node(self, node, data):
        if not node:
            return Node(data)

        if node.data > data:
            node.left_child = self.insert_node(node.left_child, data)
        else:
            node.right_child = self.insert_node(node.right_child, data)

        return node

    def remove(self, data):
        self.root = self.remove_node(self.root, data)

    def remove_node(self, node, data):
        if not node:
            return None

        if data < node.data:
            node.left_child = self.remove_node(node.left_child, data)
        elif data > node.data:
            node.right_child = self.remove_node(node.right_child, data)
        else:
            if not node.left_child and not node.right_child:
                print("Deleting Leaf Node")
                del node
                return None
            elif node.left_child and not node.right_child:
                print("Deleting Node with Left Child")
                temp_node = node.left_child
                del node
                return temp_node
            elif node.right_child and not node.left_child:
                print("Deleting Node with Right Child")
                temp_node = node.right_child
                del node
                return temp_node
            else:
                print("Deleting Node with Both Children")
                predecessor = self.get_predecessor(node.left_child)
                node.data = predecessor.data
                node.left_child = self.remove_node(node.left_child, predecessor.data)

                # successor = self.get_successor(node.right_child)
                # node.data = successor.data
                # node.right_child = self.remove_node(node.right_child, successor.data)

        return node

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)

        return node


    def get_successor(self, node):
        if node.left_child:
            return self.get_successor(node.left_child)

        return node


bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(1)
bst.insert(4)
bst.insert(10)
bst.insert(9)
bst.insert(12)
bst.in_order_traverse()
bst.remove(1)
bst.in_order_traverse()
bst.insert(1)
bst.in_order_traverse()
bst.remove(5)
bst.in_order_traverse()


