from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from os import path
import json

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
world.print_rooms()

player = Player(world.starting_room)





# Helper functions
# reverse direction helper


# BFS returning shortest path to specified node
def bfs(starting_vertex, destination_vertex, get_neighbors):
    
    starting_path = [starting_vertex]
    q = [starting_path]
    visited = set()
   
    while len(q) > 0:
      
        current_path = q.pop(0)
        current_vertex = current_path[-1]
        
        if current_vertex not in visited:

            if str(current_vertex) == str(destination_vertex):
                return current_path
        
            visited.add(current_vertex)
          
            for neighbor in get_neighbors(current_vertex):
                q.append(current_path.copy() + [neighbor])

# dft to traverse to every node    
def dft(starting_room, get_neighbors):

    traversal = []
    s = [starting_room]
    visited = set()

    while len(s) > 0:
        current = s.pop()
        if current not in visited:
            
            traversal.append(current)
            visited.add(current)

            for neighbor in get_neighbors(current):
                s.append(neighbor)
    return traversal

# get neighbors function

def get_neighbors(current):
    neighbors = list(room_graph[current][1].values())
    return neighbors

def get_direction(current, next_room):
    direction = ''
    for key, value in room_graph[current][1].items():
        if value == next_room:
            return key

# Steps:

# 1: create the traversal using BFT

traversal = dft(world.starting_room.id, get_neighbors)

# 2. loop through the array traversal and fill in gap segments with find shortest path BFS

traversal_no_gaps = []


for i in range(len(traversal) - 1):
    traversal_no_gaps.append(traversal[i])
    if traversal[i + 1] not in get_neighbors(traversal[i]):
        gap = bfs(traversal[i], traversal[i + 1], get_neighbors)[1:-1]
        traversal_no_gaps = traversal_no_gaps + gap
traversal_no_gaps.append(traversal[-1])

# 3. Convert the final traversal array into cardinal directions

# # Fill this out with directions to walk

traversal_path = []

for i in range(0, len(traversal_no_gaps) - 1):
    traversal_path.append(get_direction(traversal_no_gaps[i], traversal_no_gaps[i + 1]))


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room.id)

for move in traversal_path:

    player.travel(move)
    
    visited_rooms.add(player.current_room.id)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
