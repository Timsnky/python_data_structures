"""
Get Length
Insert at the start
Insert at the end
Traverse List
Remove Item
"""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def get_length(self):
        return self.length

    def get_length2(self):
        length = 0

        node = self.head

        while node is not None:
            length += 1
            node = node.next_node

        return length

    def insert_start(self, data):
        node = Node(data)
        self.length += 1

        node.next_node = self.head
        self.head = node

    def insert_end(self, data):
        node = Node(data)
        self.length += 1

        current_node = self.head

        if current_node is None:
            self.head = node
            return

        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = node

    def traverse_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    def remove_item(self, data):
        current_node = self.head
        item_found = False

        if current_node is None:
            return "Item not found"

        previous_node = None

        while current_node is not None:
            if current_node.data is data:
                item_found = True
                break
            else:
                previous_node = current_node
                current_node = current_node.next_node

        if item_found:
            if previous_node is not None:
                previous_node.next_node = current_node.next_node
            else:
                self.head = None
        else:
            return "Item not Found"
