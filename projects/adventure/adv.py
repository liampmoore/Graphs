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

reverse = {}
reverse['n'] = 's'
reverse['s'] = 'n'
reverse['w'] = 'e'
reverse['e'] = 'w'


# this will create a graph representation of the connections in the maze
if path.exists('graph.json'):
    with open('graph.json') as json_file: 
        graph = json.load(json_file)
else:
    graph = {}
    complete = set()
    while len(complete) < 500:
        previous = player.current_room.id
        direction = random.choice(player.current_room.get_exits())
        player.travel(direction)
        if player.current_room.id not in graph:
            graph[player.current_room.id] = {}
            for d in player.current_room.get_exits():
                graph[player.current_room.id][d] = '?'
        graph[player.current_room.id][reverse[direction]] = previous
        if '?' not in graph[player.current_room.id].values():
            complete.add(player.current_room.id) 
        for room_id in graph:
            graph[room_id] = {neighbor_id:direction for direction, neighbor_id in graph[room_id].items()}
    with open("graph.json", "w") as json_file:  
        json.dump(graph, json_file) 




# Fill this out with directions to walk

traversal_path = []





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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
