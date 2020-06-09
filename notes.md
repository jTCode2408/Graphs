- class notes -

Graphs
=======

Nodes == Verts == Vertices == Vertexes
   -Thing that stores data

Edges - connect nodes
    -Can be unidirectional, or bidirectional
    

If a graph has directional edges = 'directed graph'

Traversals
==========

Keep track of what nodes have been visisted:
    *Visited flag
    *Hashtable
    *Set


Done traversing when stack is empty:
Push starting note to top of stack
while stack is not empty: do traversal
pop value off stack, mark visited, push neighbors to stack, repeat until stack is empty


===============================================

DFS:
Depth First Traversal:
======================
Initialize stack w staring node
while stack isnt empty:
    start at top of stack, if node not visited:
        mark as visited
        add neighbors to stack
        go back to top of stack-repeat
    REPEAT UNTIL STACK EMPTY



BFS:
def bfs(self, starting_vertex_id, target_vertex_id):
    # Create an empty queue and enqueue A PATH TO the starting vertex ID
    # Create a Set to store visited vertices
    # While the queue is not empty...
        # Dequeue the first PATH
        # Grab the last vertex from the PATH
        # If that vertex has not been visited...
            # CHECK IF IT'S THE TARGET
              # IF SO, RETURN PATH
            # Mark it as visited...
            # Then add A PATH TO its neighbors to the back of the queue
              # COPY THE PATH
              # APPEND THE NEIGHOR TO THE BACK












