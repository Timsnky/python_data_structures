class Node(object):

    def __init__(self, data):
        self.data = data
        self.adjacency_list = []
        self.visited = False


class BreadthFirstSearch(object):

    def bfs(self, start_node):
        queue = []
        queue.append(start_node)

        while queue:
            current_node = queue.pop(0)
            current_node.visited = True
            print(current_node.data)

            for child_node in current_node.adjacency_list:
                if not child_node.visited:
                    queue.append(child_node)



if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)
    node5.adjacency_list.append(node1)

    bfs = BreadthFirstSearch()
    bfs.bfs(node1)