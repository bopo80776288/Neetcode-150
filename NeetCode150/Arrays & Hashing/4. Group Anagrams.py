from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if strs are said to be anagrams they should have exact same character counts
        # we want to creat a list that includes 26 lists of each character count, and asign the list to each str as a key
        # we want to then group the strs that has the same character count list to a sublist
        # we need a hashtable that matches (character count [] * 26) : str 
        wordhash = defaultdict(list)
        for str in strs:
            count = [0] * 26 
            for c in str:
                count[ord(c) - ord('a')] += 1 
            wordhash[tuple(count)].append(str)
        return wordhash.values()
    
        # defaultdict(list): Avoids manual initialization of lists.
        # tuple(count): Converts the mutable list to an immutable, hashable key.

# Test cases
solution = Solution()

# Example test case 1
strs=["act","pots","tops","cat","stop","hat"]
print(solution.groupAnagrams(strs)) 

# Key Takeaway Notes:
# Dictionaries are unhashable, so they cannot be used as keys.
# If they were hashable, order wouldn’t matter (they compare based on key-value pairs).
# Tuples are ordered, so different key orders result in different keys.
# Sorting dict.items() ensures a consistent tuple representation, preventing unordered dictionary keys from causing incorrect anagram groupings.
# In this case we want to avoid sorting so we use a [0] * 26 list instead
# Converting the list to a tuple (tuple(count)) makes it hashable, allowing it to be used as a key in wordhash.