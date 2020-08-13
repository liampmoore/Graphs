## Project Goals:
### Fill the 'traversal_path' list in adv.py with a complete traversal of the graph


## figure out how to get to every neighbor from every single node
- brute force, randomly walk around until you have a complete traversal graph of 500 complete items lmao, then save it to json to save time

## Use this Traversal Graph Iterative DFT
- use an iterative DFT with the saved graph
- save the path you take down to each node until you hit dead end or visited nodes
- when you hit a dead end nested while loop back up the path, adding reverse path until you have unvisited neighbors again
- iterate through the path of NODE IDS and convert them to directions

### Limitations
- you can't skip around the graph, you can only move to connected nodes
- the only way you can learn the id of a node is by moving to it


### Further thoughts/ stretch
- there are ways you can skip through certain visited nodes to save time getting to unvisited nodes
- maybe you could do a nested shortest path BFS to get to the next unvisited node instead of a nested reverse path
- optimize the first half of the problem somehow