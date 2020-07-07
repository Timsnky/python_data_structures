
class Node(object):

    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    # O(log N) or O (N) if unbalanced
    def insert(self, data):
        if self.root:
            self.insert_node(self.root, data)
        else:
            self.root = Node(data)

    def insert_node(self, node, data):
        if node.data > data:
            if node.left_child:
                self.insert_node(node.left_child, data)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insert_node(node.right_child, data)
            else:
                node.right_child = Node(data)

    # O(log N) or O (N) if unbalanced
    def remove(self, data):
        if self.root:
            self.root = self.remove_node(self.root, data)

    def remove_node(self, node, data):
        if not node:
            return node

        if node.data > data:
            node.left_child = self.remove_node(node.left_child, data)
        elif node.data < data:
            node.right_child = self.remove_node(node.right_child, data)
        else:
            if not node.left_child and not node.right_child:
                print("Removing a leaf node")
                del node
                return None
            elif not node.left_child:
                print("Removing node with right child")
                temp_node = node.right_child
                del node
                return temp_node
            elif not node.right_child:
                print("Removing node with left child")
                temp_node = node.left_child
                del node
                return temp_node
            else:
                print("Removing a node with two children")
                predecessor = self.get_predecessor(node.left_child)
                node.data = predecessor.data
                node.left_child = self.remove_node(node.left_child, predecessor.data)

        return node

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)

        return node

    # O(log N) or O (N) if unbalanced
    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.left_child:
            return self.get_min(node.left_child)

        return node.data

    # O(log N) or O (N) if unbalanced
    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.right_child:
            return self.get_max(node.right_child)

        return node.data

    # O(N)
    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)

        print(str(node.data) + " ")

        if node.right_child:
            self.traverse_in_order(node.right_child)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(14)
# bst.remove(10)

print(bst.get_min_value())
print(bst.get_max_value())
bst.traverse()

