import random
from util import Stack, Queue 
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        # !!!! IMPLEMENT ME

        if num_users < avg_friendships:
            raise ValueError('Average friendships can not exceed the number of users.')

        # Add users
        for i in range(1, num_users + 1):
            self.add_user(i)

        # Create friendships

        # loop through range of user ids
        for user_id in range(1, num_users + 1):
            # loop a random amount from zero to twice the average
            for i in range(random.randint(0, avg_friendships)):
                # pick a random key from the list of existing users
                friend_id = random.choice(list(self.users.keys()))
                # make sure the key isn't already in the friends list to prevent overwriting,
                # which ensures our given number for average friends will be accurate
                while friend_id in self.friendships[user_id] or user_id == friend_id:
                    friend_id = random.choice(list(self.users.keys()))
                # add that random key the current user's friend list
                self.add_friendship(user_id, friend_id)
      

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

                # create a queue and enqueue a starting verted
        q = Queue()
        q.enqueue([user_id])

        # while the queue is not empty
        while len(q) > 0:
            # deque the path
            current_path = q.dequeue()
            current_vertex = current_path[-1]
            # if vertex has not been visited
            if current_vertex not in visited:
                # mark it as visited
                visited[current_vertex] = current_path
                # loop through neighbors
                for friend in self.friendships[current_vertex]:
                    # enqueue each one
                    q.enqueue(current_path.copy() + [friend])
            else:
                if len(current_path) < len(visited[current_vertex]):
                    visited[current_vertex] = current_path

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print(connections)

    total = 0
    
    for friends in sg.friendships.values():
        total += len(friends)

    average = total/len(sg.friendships)

    print(average)
