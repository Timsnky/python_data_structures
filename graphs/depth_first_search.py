class Node(object):

    def __init__(self, data):
        self.data = data
        self.adjacency_list = []
        self.visited = False
        self.predecessor = None


class DepthFirstSearch(object):

    def dfs(self, node):
        node.visited = True
        print(node.data)

        for node in node.adjacency_list:
            if not node.visited:
                self.dfs(node)

    def dfs2(self, start_node):
        stack = []
        stack.append(start_node)
        start_node.visited = True

        while stack:

            node = stack.pop(-1)
            print(node.data)

            for child in node.adjacency_list[::-1]:
                if not child.visited:
                    child.visited = True
                    stack.append(child)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node6)
node1.adjacency_list.append(node7)
node2.adjacency_list.append(node3)
node2.adjacency_list.append(node4)
node4.adjacency_list.append(node5)
node7.adjacency_list.append(node8)

dfs = DepthFirstSearch()
dfs.dfs2(node1)



