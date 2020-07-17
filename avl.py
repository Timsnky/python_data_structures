
class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left_child = None
        self.right_child = None


class AVL(object):
    
    def __init__(self):
        self.root = None

    def calculate_height(self, node):

        if not node:
            return -1

        return node.height

    def calculate_balance(self, node):
        """
        If return is > 1 Left child is heavy thus rotate to right
        If return is < -1 right child is heavy thus rotate to left
        @param node:
        @return:
        """
        if not node:
            return 0

        return self.calculate_height(node.left_child) - self.calculate_height(node.right_child)

    def rotate_right(self, node):

        print("Rotating to the right on node " + str(node.data))
        temp_left_child = node.left_child
        t = temp_left_child.right_child

        node.left_child = t
        temp_left_child.right_child = node

        node.height = max(self.calculate_height(node.left_child), self.calculate_height(node.right_child)) + 1
        temp_left_child.height = max(self.calculate_height(temp_left_child.left_child), self.calculate_height(temp_left_child.right_child)) + 1

        return temp_left_child

    def rotate_left(self, node):
        print("Rotating to the left on node " + str(node.data))

        temp_right_child = node.right_child
        t = temp_right_child.left_child

        node.right_child = t
        temp_right_child.left_child = node

        node.height = max(self.calculate_height(node.left_child), self.calculate_height(node.right_child)) + 1
        temp_right_child.height = max(self.calculate_height(temp_right_child.left_child), self.calculate_height(temp_right_child.right_child)) + 1

        return temp_right_child

    def traverse(self):
        if self.root:
            return self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)

        print(node.data)

        if node.right_child:
            self.traverse_in_order(node.right_child)

    def insert(self, data):
        self.root = self.insert_node(self.root, data)

    def insert_node(self, node, data):
        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert_node(node.left_child, data)
        else:
            node.right_child = self.insert_node(node.right_child, data)
            
        node.height = max(self.calculate_height(node.left_child), self.calculate_height(node.right_child)) + 1
        
        return self.settle_violation(node, data)

    def settle_violation(self, node, data):
        balance = self.calculate_balance(node)

        if balance > 1 and data < node.left_child.data:
            print("Left left heavy tree ...")
            return self.rotate_right(node)

        if balance > 1 and data >= node.left_child.data:
            print("Left right heavy tree ...")
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)

        if balance < -1 and data >= node.right_child.data:
            print("Right right heavy tree ...")
            return self.rotate_left(node)

        if balance < -1 and data < node.right_child.data:
            print("Right left heavy tree ...")
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def remove(self, data):
        if self.root:
            self.root = self.remove_node(self.root, data)

    def remove_node(self, node, data):

        if data > node.data:
            node.right_child = self.remove_node(node.right_child, data)
        elif data < node.data:
            node.left_child = self.remove_node(node.left_child, data)
        else:
            if not node.left_child and not node.right_child:
                print("Removing leaf node")
                del node
                return None

            if not node.right_child:
                print("Removing node with left child")
                temp_left = node.left_child
                del node
                return temp_left

            if not node.left_child:
                print("Removing node with right child")
                temp_right = node.right_child
                del node
                return temp_right

            print("Removing node with two children")
            predecessor = self.get_predecessor(node.left_child)
            node.data = predecessor.data
            node.left_child = self.remove_node(node.left_child, predecessor.data)

            if not node:
                return node

            node.height = max(self.calculate_height(node.right_child), self.calculate_height(node.left_child))

            return self.settle_remove_violations(node)

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)

        return node

    def settle_remove_violations(self, node):
        balance = self.calculate_balance(node)

        if balance > 1:
            left_balance = self.calculate_balance(node.left_child)

            if left_balance >= 0:
                return self.rotate_right(node)
            else:
                node.left_child = self.rotate_left(node.left_child)
                return self.rotate_right(node)

        if balance < -1:
            right_balance = self.calculate_balance(node.right_child)

            if right_balance >= 0:
                return self.rotate_left(node)
            else:
                node.right_child = self.rotate_right(node.right_child)
                return self.rotate_left(node)

        return node


avl = AVL()
avl.insert(10)
avl.insert(5)
avl.insert(6)

