
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

    def insert_start(self, data):
        new_node = Node(data)
        self.length += 1

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        self.length += 1
        current_node = self.head

        while current_node.next_node is not Node:
            current_node = current_node.next_node

        current_node.next_node = new_node

    def traverse_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)

    def remove_item(self, data):
        current_node = self.head
        previous_node = None
        found = False

        while current_node:
            if current_node.data is data:
                found = True
                break
            else:
                current_node = current_node.next_node
                previous_node = current_node

        if found is False:
            return "Item not found"
        else:
            if previous_node is None:
                self.head = current_node.next_node
            else:
                previous_node.next_node = current_node.next_node

ll = LinkedList()
ll.insert_end(2)