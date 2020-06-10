from util import Queue

''''
 graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
 =============================
  graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
  ============================
  * The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.
============================================
Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual
''''
#need to get neighbors for each vert(child)
#nkey = index('unique identifier)
#value = vert
##relationships = edges
#data is a list()
#use Queue?
#need to keep track of path
#



def earliest_ancestor(ancestors, starting_node):
#bfs search for paths
    q = Queue()
    q.enqueue([starting_node])
    neighbor_path=1
    furthest=-1

    while q.size()>0:
        path =q.dequeue()
        vert =path[-1]




    return furthest


