class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 0


class AVL(object):

    def __init__(self):
        self.root = None

    def get_max_value(self):
        if self.root:
            node = self.get_max_node(self.root)
            return node.data

    def get_max_node(self, node):
        if node.right_child:
            return self.get_max_node(node.right_child)

        return node

    def get_min_value(self):
        if self.root:
            node = self.get_min_node(self.root)
            return node.data

    def get_min_node(self, node):
        if node.left_child:
            return self.get_min_node(node.left_child)

        return node

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert_node(data, node.left_child)
        else:
            node.right_child = self.insert_node(data, node.right_child)

        node.height = self.calculate_height(node)

        return self.settle_violations(node, data)

    def remove(self, data):
        self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return None

        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)
        else:
            if not node.right_child and not node.left_child:
                del node
                node = None
            elif node.left_child and not node.right_child:
                temp_node = node.left_child
                del node
                node = temp_node
            elif node.right_child and not node.left_child:
                temp_node = node.right_child
                del node
                node = temp_node
            else:
                predecessor = self.get_predecessor(node.left_child)
                node.data = predecessor.data
                node.left_child = self.remove_node(predecessor.data, node.left_child)

                """
                successor = self.get_successor(node.right_child)
                node.data = successor.data
                node.right_child = self.remove_node(successor.data, node.right_child)
                """
        if not node:
            return node

        node.height = self.calculate_height(node)

        return self.settle_violations(node, data)

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)

        return node

    def get_successor(self, node):
        if node.left_child:
            return self.get_successor(node.left_child)

        return node

    def traverse(self):
        if self.root:
            return self.traverse_node(self.root)

    def traverse_node(self, node):
        if node.left_child:
            self.traverse_node(node.left_child)

        print(node.data)

        if node.right_child:
            self.traverse_node(node.right_child)

    def get_height(self, node):
        if not node:
            return -1

        return node.height

    def calculate_height(self, node):
        return max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1

    def calculate_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left_child) - self.get_height(node.right_child)

    def rotate_right(self, node):
        temp_node = node.left_child
        node.left_child = temp_node.right_child
        temp_node.right_child = node

        node.height = self.calculate_height(node)
        temp_node.height = self.calculate_height(temp_node)

        return temp_node

    def rotate_left(self, node):
        temp_node = node.right_node
        node.right_node = temp_node.left_node
        temp_node.left_node = node

        node.height = self.calculate_height(node)
        temp_node.height = self.calculate_height(temp_node)

        return temp_node

    def settle_violations(self, node, data):
        balance = self.calculate_balance(node)

        if balance > 1:
            if data < node.left_child.data:
                # Left Left Heavy
                return self.rotate_right(node)
            else:
                # Left Right Heavy
                node.left_child = self.rotate_left(node.left_child)
                return self.rotate_right(node)

        if balance < -1:
            if data > node.right_child.data:
                # Right Right Heavy
                return self.rotate_left(node)
            else:
                # Right Left Heavy
                self.right_child = self.rotate_right(self.right_child)
                return self.rotate_left(node)

        return node
