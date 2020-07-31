class Node(object):

    def __init__(self, data):
        self.data = data
        self.adjacency_list = []
        self.visited = False
        self.predecessor = None


class BreadthFirstSearch(object):

    def bfs(self, start_node):

        queue = []
        start_node.visited = True
        queue.append(start_node)

        while queue:

            node = queue.pop(0)
            print(node.data)

            for child in node.adjacency_list:
                if not child.visited:
                    child.visited = True
                    queue.append(child)



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

    bfs = BreadthFirstSearch()
    bfs.bfs(node1)