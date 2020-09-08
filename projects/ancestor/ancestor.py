from graph import Graph, Queue

'''
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
'''
#need to get neighbors for each vert(child)
#nkey = index('unique identifier)
#value = vert
##relationships = edges
#data is a list()
#use Queue?
#need to keep track of path
#need paths stored
#

def earliest_ancestor(ancestors, starting_node):
    graph =Graph()
    visited = set()
    #save each path as go
    paths =dict()

#make parent.child pair
#check if visited, if not, visit/add to visited
    for pair in ancestors:
        parent, child = pair
        if parent not in visited:
            visited.add(parent)
        if child not in visited:
            visited.add(child)
            #initialize grapdh
    for vert in visited:
        graph.add_vertex(vert)
        #initialize paths to keep track
        paths[vert] =[]
#add eges for pair relations
#child to parent 
    for pair in ancestors:
        parent, child =pair
        graph.add_edge(child, parent)

#verts to visit, /keep track of
    to_visit =Queue()
    to_visit.enqueue(starting_node)
#check queue for verts to visit
    while to_visit.size() >0 :
        current = to_visit.dequeue()
#get parent of current node
#getath from current 
#keep track of paths taken
        for parent in graph.get_neighbors(current):
            copy_path =paths[current][:]
            copy_path.append(current)
            paths[parent] =copy_path

            to_visit.enqueue(parent)
#full path once reach end, current vert added to path

        full_path = paths[current][:]
        full_path.append(current)
        paths[current] =full_path
#hold longest paths
    longest=[]

#check paths, find longest
#last item in path will be furthest
    for node in paths:
        current = paths[node]
        if len(current) > len(longest):
            longest = current
            
    if len(longest) ==1:
        return -1

    return longest[-1]

    