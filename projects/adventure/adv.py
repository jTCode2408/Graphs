from room import Room
from player import Player
from world import World
from util import Stack
import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# Print an ASCII map
#world.print_rooms()

####################PLanning####################

#dft(stack)
#need to be able to go back!
#keep track of opposite direction entered(go back)
#keep track of path(visited exits)
#keep track of room in
#keep track of directions(exits) rooms visited(for going back)---room has [get_exits] & [get_room_in_directions] fn
#player has [travel] fn to move

#TODO--Traversal code(done)
#keep track of visited rooms(set)
#keep path in stack
#rooms len for all rooms checked
#while rooms not visited:
#check exits in room
#keep track of moves
#keep track of exits for room
#if room move direction hasnt been visited, visit(Add to visited) --add exits to moves
#add room to visited
#check for directions
#get ran direction from omves avail
#visit room
#add to paths
#if no exits: go back!
#to go back:
#no exits in room
#go opposite of last move
#add path
#get last move, travel that way

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


#use opposite of last direction entered to go back
def opposite_way(direction):
    if direction == 'n':
        return 's'
    elif direction =='s':
        return 'n'
    elif direction =='w':
        return 'e'
    elif direction == 'e':
        return 'w'

visited = set()
paths= Stack()

while len(visited) < len(world.rooms):

    exits = player.current_room.get_exits()
    moves = []

    for exit in exits:
        if exit is not None and player.current_room.get_room_in_direction(exit) not in visited:
            moves.append(exit)
    visited.add(player.current_room)
   
    if len(moves) >0:
        random_dir = random.randint(0, len(moves) -1)
        player.travel(moves[random_dir])
        paths.push(moves[random_dir])
        traversal_path.append(moves[random_dir])

    else:
        go_back = paths.pop()
        player.travel(opposite_way(go_back))
        traversal_path.append(opposite_way(go_back))



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
