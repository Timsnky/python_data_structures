import heapq
import sys

class Edge(object):

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacency_list = []
        self.min_distance = sys.maxsize

    def __cmp__(self, other_vertex):
        return self.cmp(self.min_distance, other_vertex.min_distance)

    def __lt__(self, other_vertex):
        return self.min_distance < other_vertex.min_distance


class Dijkstra(object):

    def calculate_shortest_path(self, start_vertex):
        queue = []
        start_vertex.min_distance = 0
        heapq.heappush(queue, start_vertex)

        while queue:
            current_vertex = heapq.heappop(queue)

            for edge in current_vertex.adjacency_list:
                start = edge.start_vertex
                end = edge.target_vertex
                new_distance = start.min_distance + edge.weight

                if new_distance < end.min_distance:
                    end.predecessor = start
                    end.min_distance = new_distance
                    heapq.heappush(queue, end)

    def get_shortest_path(self, target_vertex):
        print("Shortest path to vertex is : " + str(target_vertex.min_distance))

        while target_vertex:
            print (target_vertex.name)
            target_vertex = target_vertex.predecessor


vertex1 = Vertex("A")
vertex2 = Vertex("B")
vertex3 = Vertex("C")
vertex4 = Vertex("D")
vertex5 = Vertex("E")
vertex6 = Vertex("F")
vertex7 = Vertex("G")
vertex8 = Vertex("H")

edge1 = Edge(5,vertex1,vertex2)
edge2 = Edge(8,vertex1,vertex8)
edge3 = Edge(9,vertex1,vertex5)
edge4 = Edge(15,vertex2,vertex4)
edge5 = Edge(12,vertex2,vertex3)
edge6 = Edge(4,vertex2,vertex8)
edge7 = Edge(7,vertex8,vertex3)
edge8 = Edge(6,vertex8,vertex6)
edge9 = Edge(5,vertex5,vertex8)
edge10 = Edge(4,vertex5,vertex6)
edge11 = Edge(20,vertex5,vertex7)
edge12 = Edge(1,vertex6,vertex3)
edge13 = Edge(13,vertex6,vertex7)
edge14 = Edge(3,vertex3,vertex4)
edge15 = Edge(11,vertex3,vertex7)
edge16 = Edge(9,vertex4,vertex7)

vertex1.adjacency_list.append(edge1)
vertex1.adjacency_list.append(edge2)
vertex1.adjacency_list.append(edge3)
vertex2.adjacency_list.append(edge4)
vertex2.adjacency_list.append(edge5)
vertex2.adjacency_list.append(edge6)
vertex8.adjacency_list.append(edge7)
vertex8.adjacency_list.append(edge8)
vertex5.adjacency_list.append(edge9)
vertex5.adjacency_list.append(edge9)
vertex5.adjacency_list.append(edge10)
vertex5.adjacency_list.append(edge11)
vertex6.adjacency_list.append(edge12)
vertex6.adjacency_list.append(edge13)
vertex3.adjacency_list.append(edge14)
vertex3.adjacency_list.append(edge15)
vertex4.adjacency_list.append(edge16)


vertexList = (vertex1,vertex2,vertex3, vertex4, vertex5, vertex6, vertex7, vertex8)

algorithm = Dijkstra()
algorithm.calculate_shortest_path(vertex1)
algorithm.get_shortest_path(vertex4)
