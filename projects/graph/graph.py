"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError("Vertex does not exist.")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue and enqueue a starting verted
        q = Queue()
        q.enqueue(starting_vertex)
        # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty
        while len(q) > 0:
            # deque the first vertex
            current = q.dequeue()
            # if vertex has not been visited
            if current not in visited:
                # mark it as visited
                visited.add(current)
                print(current)
                # loop through neighbors
                for neighbor in self.get_neighbors(current):
                    # enqueue each one
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        
         # create a queue and enqueue a starting verted
        s = Stack()
        s.push(starting_vertex)
        # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty
        while len(s) > 0:
            # deque the first vertex
            current = s.pop()
            # if vertex has not been visited
            if current not in visited:
                # mark it as visited
                visited.add(current)
                print(current)
                # loop through neighbors
                for neighbor in self.get_neighbors(current):
                    # enqueue each one
                    s.push(neighbor)
        return visited

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue the path to the starting vertex id
        starting_path = [starting_vertex]
        q = Queue()
        q.enqueue(starting_path)
        # create a set to store visited vertices
        visited = set()
        # while queueu not empty
        while len(q) > 0:
            # dequeue the first path
            current_path = q.dequeue()
            # grab the last vertex from the path
            current_vertex = current_path[-1]
            # if vertex is not in visited
            if current_vertex not in visited:
                # check if it is the target
                if current_vertex == destination_vertex:
                    # return the path to the target
                    return current_path
                # mark it visited
                visited.add(current_vertex)
                # add path to naighbours to back of queue
                for neighbor in self.get_neighbors(current_vertex):
                    q.enqueue(current_path.copy() + [neighbor])
                    # copy the path
                    # append the neighbor to the back of it
        # return none
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty queue and enqueue the path to the starting vertex id
        starting_path = [starting_vertex]
        s = Stack()
        s.push(starting_path)
        # create a set to store visited vertices
        visited = set()
        # while queueu not empty
        while len(s) > 0:
            # dequeue the first path
            current_path = s.pop()
            # grab the last vertex from the path
            current_vertex = current_path[-1]
            # if vertex is not in visited
            if current_vertex not in visited:
                # check if it is the target
                if current_vertex == destination_vertex:
                    # return the path to the target
                    return current_path
                # mark it visited
                visited.add(current_vertex)
                # add path to naighbours to back of queue
                for neighbor in self.get_neighbors(current_vertex):
                    s.push(current_path.copy() + [neighbor])
                    # copy the path
                    # append the neighbor to the back of it
        # return none
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # create a new path that includes the current vertex
        path = path + [starting_vertex]

        # if you have reached the destination return the current path
        if starting_vertex == destination_vertex:
            return path
       
        # create a variable to hold the shortest path starting as None
        shortest = None

        # loop through each neighbor of the current vertex
        for neighbor in self.get_neighbors(starting_vertex):
            # if you haven't visited the neighbor
            if neighbor not in visited:
                # vadd the neighbor to visited
                visited.add(neighbor)
                # recursively call the function to get a path from the neighbor to the end
                neighborpath = self.dfs_recursive(neighbor, destination_vertex, path.copy())
                # if the call of this function on the current neighbor found a path to the end
                if neighborpath is not None:
                    # if shortest is None change shortest to the neighborpath
                    if shortest is None:
                        shortest = neighborpath
                    # otherwise check if the current neighborpath is shorter than shortest
                    elif len(neighborpath) < len(shortest):
                        # if so, change the shortest
                        shortest = neighborpath
        # if no path to the end was found in any recursive calls shortest will be None
        # otherwise we will have looped through all paths and found the shortest
        return shortest

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
