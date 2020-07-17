
class Node(object):

    def __init__(self, character):
        self.character = character
        self.right_node = None
        self.left_node = None
        self.middle_node = None
        self.value = 0


class TST(object):

    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value, 0)

    def put_item(self, node, key, value, index):

        character = key[index]

        if not node:
            node = Node(character)

        if character < node.character:
            node.left_node = self.put_item(node.left_node, key, value, index)
        elif character > node.character:
            node.right_node = self.put_item(node.right_node, key, value, index)
        elif index < len(key) - 1:
            node.middle_node = self.put_item(node.middle_node, key, value, index + 1)
        else:
            node.value = value

        return node

    def get(self, key):

        node = self.get_item(self.root, key, 0)

        if not node:
            return -1

        return node.value

    def get_item(self, node, key, index):

        if not node:
            return None

        character = key[index]

        if character < node.character:
            return self.get_item(node.left_node, key, index)
        elif character > node.character:
            return self.get_item(node.right_node, key, index)
        elif index < len(key) - 1:
            return self.get_item(node.middle_node, key, index + 1)
        else:
            return node


tst = TST()
tst.put('carrot', 100)

print(tst.get("carrot"))



