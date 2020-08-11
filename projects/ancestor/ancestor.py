
def earliest_ancestor(ancestors, starting_node, current_node = None, path = None, longest = None):
    # if the table is not a hash table convert it to a hash table for convenience
    if type(ancestors) == list:
        table = {}
        for (parent, child) in ancestors:
            if child not in table:
                table[child] = [parent]
            else:
                table[child].append(parent)
        ancestors = table
    # set the current node to the starting node
    if current_node is None:
        current_node = starting_node

    # if the path has not been initialize yet set it to the starting node
    if path is None:
        path = [starting_node]
    # otherwise we are on a recursive call and we must add the current node to the path
    else:
        path = path + [current_node]
    
    # initialize longest path as the current path
    longest = path

    # if the current node has ancestors
    if current_node in ancestors:
        # loop through it's ancestors
        for ancestor in ancestors[current_node]:
            # find the longest path for each ancestor
            ancestor_path = earliest_ancestor(ancestors, starting_node, ancestor, path.copy(), longest.copy())
            # if the path via the ancestor is longer set the longest to that ancestor path
            if len(ancestor_path) > len(longest):
                longest = ancestor_path
            # if it is equal to the longest take the path with the lower integer key for furthest ancestor
            elif len(ancestor_path) == len(longest):
                if ancestor_path[-1] < longest[-1]:
                    longest = ancestor_path

    # if the starting node has no ancestors return -1
    if starting_node not in ancestors:
        return -1
    # if we are at the top call return the furthest ancestor
    elif current_node == starting_node:
        return longest[-1]
    # if we aren't at the top call return the longest path for current ancestor branch
    else:
        return longest



# Input: A list of (parent, child) pairs, ONE single node.
# Output: The earliest ancestor of two nodes. That is, the furthest ancestor node from both children. Tied ancestors go with the lowest numeric ID.

# Conditions: 
# * The input will not be empty.
# * There are no cycles in the input.
# * If an ancestor and child are connected, it is by exactly one path. So caching paths would not speed this up, it seems.
# * IDs will always be positive integers.
# * A parent may have any number of children.

# Plan overview: Use a recursive DFT approach to generate paths, while iterating through neighbor paths keep track of the longest path and change it if it meets spec. Return the value of the furthest path.


# Step 1: Convert ancestors data to a hash table if it isn't already, with the child as a key and an array of ancestors as a value.

# Step 2: Create a variable to keep track of longest path and initialize it as None.

# Step 3: Loop through ancestors of starting node.

# Step 4: For each ancestor, recursively call the function to create a path for that ancestor and check if that path meets conditions.

# Step 5: Return the longest path that meets the specified conditions.