
class Node(object):

    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.leftChild = None


class BST(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(self.root, data)


        self.insert_node(node)