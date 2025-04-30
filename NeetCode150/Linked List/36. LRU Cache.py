class Node:
    def __init__(self, key, val):
        # self.something is to create an instance of the input variable 
        self.key, self.val = key, val
        # assign a double linked list structure 
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # keep the input capacity to the instance self.cap
        self.cap = capacity
        # create a hashmap to map key:node
        self.cache = {}  # map key to node
        # create dummy nodes for keeping track of the least recent used (lru) and most recent used(mru)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # we have a node input and we want to remove it, so the logic is to set the prev of the node to link to next of the node 
        # by that we skip the input node, which is the same as removing it
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # we have a node input and want to insert it
        # as the inserting node will always be the most recent use, we know to insert it to the left of the mru dummy node 
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        # by definition of get, check if is in hashmap, if in we need to change its position to mru 
        # so go through remove and then insert, finally return the .val of it 
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        # if not in hashmap return -1 
        return -1

    def put(self, key: int, value: int) -> None:
        # by definition of put, check if it is in hashmap, if yes we will remove it 
        if key in self.cache:
            self.remove(self.cache[key])
        # assign key to the create node 
        self.cache[key] = Node(key, value)
        # insert 
        self.insert(self.cache[key])

        # one more condition to check that if the total cache exceeds the max capacity
        # find the lru node by self.left.next, and remove it and also delete it from hashmap 
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]