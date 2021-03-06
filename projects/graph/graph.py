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
            raise IndexError('Error, no vertex')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create que to pop nodes onto
        #add starting node to que
        #create a set for visisted nodes
        #while queue not empty:
        #dequeue first node
        #if not in visited:
        #visit, add to visited, and add neighbors to queue  
        q = Queue()
        #pop onto queue
        q.enqueue(starting_vertex)
        visited =set()

        #while queue isnt empty
        while q.size() > 0:
            vert =q.dequeue()
        #if node not in visited, add to visited(visit)
            if vert not in visited:
                visited.add(vert)
                print(vert)
                #add neighbors to queue
                for next_vert in self.get_neighbors(vert):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #create stack to pop nodes onto
        #add starting node to stack
        #create a set for visisted nodes
        #while stack not empty:
        #remove first node
        #if not in visited:
        #visit, add to visited, and add neighbors to stack  
        s = Stack()
        #pop onto stack
        s.push(starting_vertex)
        visited =set()

        #while stack isnt empty
        while s.size() > 0:
            vert =s.pop()
        #if node not in visited, add to visited(visit)
            if vert not in visited:
                visited.add(vert)
                print(vert)
                #add neighbors to stack
                for next_vert in self.get_neighbors(vert):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited =None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #base case: empty stack
        #create stack to pop nodes onto
        #add starting node to stack
        #create a set for visisted nodes
        #--recursive loop --
        #while stack not empty:
        #remove first node
        #if not in visited:
        #visit, add to visited, and add neighbors to stack  

        #while stack is empty
        
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)

        for vert in self.vertices[starting_vertex]:
            if vert not in visited:
                self.dft_recursive(vert, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited =set()

# While the queue is not empty...
			# Dequeue the first PATH
        while q.size() > 0:
            path = q.dequeue()
            # Grab the last vertex from the PATH
            vertex =path[-1]            
			# If that vertex has not been visited...
            if vertex ==destination_vertex:
            # CHECK IF IT'S THE TARGET
			# IF SO, RETURN PATH
                return path
            # Mark it as visited..
            visited.add(vertex)
            # Then add A PATH TO its neighbors to the back of the queue
            for next_vert in self.vertices[vertex]:
                neighbor_path =list(path)
                # COPY THE PATH
				  # APPEND THE NEIGHOR TO THE BACK
                neighbor_path.append(next_vert)
    # Create an empty queue and enqueue A PATH TO the starting vertex ID
                q.enqueue(neighbor_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
       #bfs, but with stack
        s = Stack()
        s.push([starting_vertex])
        visited =set()

        while s.size() > 0:
            path = s.pop()
            vertex =path[-1]            

            if vertex ==destination_vertex:
                return path
            visited.add(vertex)
            
            for next_vert in self.vertices[vertex]:
                neighbor_path =list(path)
                neighbor_path.append(next_vert)
                s.push(neighbor_path)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited =None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

           

        for vertex in self.vertices[starting_vertex]:
            if vertex not in visited:
                self.dfs_recursive(vertex,visited)
            


  


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
    print(graph.vertices)

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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
