class TimeMap:

    def __init__(self):
        # key = string, value = list of [value, timestamp]
        # initialize the hashmap structure
        self.store = {} 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key is not exist yet, assign the key to an empty list
        if key not in self.store:
            self.store[key] = []
        # assign the value, timestamp pair to the key
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # default value to return if the key doesn't even exist
        res = ""
        # we get to that specific key and pull the list 
        values = self.store.get(key, [])
        
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2 
            # valid timestamp
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1 
            # invalid timestamp
            else:
                r = mid - 1 

        return res
