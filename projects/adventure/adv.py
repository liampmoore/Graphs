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
reverse = {}
reverse['n'] = 's'
reverse['s'] = 'n'
reverse['w'] = 'e'
reverse['e'] = 'w'
# BFS shortest path
def bfs(starting_vertex, destination_vertex, graph):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    # create an empty queue and enqueue the path to the starting vertex id
    starting_path = [starting_vertex]
    q = [starting_path]
    # create a set to store visited vertices
    visited = set()
    # create a variable for shortest
    shortest = None
    # while queueu not empty
    while len(q) > 0:
        # dequeue the first path
        current_path = q.pop(0)
        # grab the last vertex from the path
        current_vertex = current_path[-1]
        # if vertex is not in visited
        if current_vertex not in visited:
            # check if it is the target
            if current_vertex == destination_vertex:
                # if the shortest is None
                if shortest is None:
                    shortest = current_path
                elif len(current_path) < len(shortest):
                    shortest = current_path
            # mark it visited
            visited.add(current_vertex)
            # add path to naighbours to back of queue
            for neighbor in graph[current_vertex].values():
                q.append(current_path.copy() + [neighbor])
                # copy the path
                # append the neighbor to the back of it
    # return None if you didn't find it, otherwise return shortest path
    return shortest


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
    with open("graph.json", "w") as json_file:  
        json.dump(graph, json_file) 




# Fill this out with directions to walk

traversal_path = []

# create a stack and push the starting verted
s = [str(world.starting_room.id)]
# create a set to store the visited vertices
visited = set()

# while the stack is not empty
while len(s) > 0:
    # pop the first vertex
    current = str(s.pop())
    # if vertex has not been visited
    if str(current) not in visited:
        
        # add it to the traversal path
        traversal_path.append(current)

        # mark it as visited
        visited.add(str(current))

        num_neighbors_pushed = 0
        # loop through neighbors
        for neighbor in graph[current].values():
            if str(neighbor) not in visited:
                # push each one
                if current == str(22):
                    print(neighbor)
                s.append(neighbor)
                num_neighbors_pushed += 1


        
        # if at a dead end we must go back up the graph before we go to the next in queue
        # use a BFS shortest path to get the path from current to the next ID in the queue
        # we only need to do this search if
        if num_neighbors_pushed == 0:
            if traversal_path[-2] in graph[s[-1]].values():
                traversal_path.append(traversal_path[-2])
            else:
                traversal_path = traversal_path + bfs(traversal_path[-1], s[-1], graph)[1:-2]


# convert the path of node ids to a path of directions

# directional_path = []
# i = 1
# current = traversal_path[0]
# for i in range(len(traversal_path)):
#     previous = current
#     current = traversal_path[i]

#     direction = None

#     for key, value in graph[previous].items():
#         if str(value) == str(current):
#             direction = key


#     print(direction)
#     directional_path.append(direction)


#     i += 1


# traversal_path = directional_path

# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

# print(traversal_path)


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
