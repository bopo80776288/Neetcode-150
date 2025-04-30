class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if two str are anagram, that means that they should have exactly the same character count that makes the word
        # set up two hash tables to count each character in the str which we will have character : count
        stable = {}
        ttable = {}

        # use the .get() function to avoid possible error of value not found for the first appearance 
        for i in s:
            stable[i] = 1 + stable.get(i, 0)
        for j in t:
            ttable[j] = 1 + ttable.get(j, 0)
        # since this is a true/false question, set return to stable == ttable can see if the two str has exact same character count
        return stable == ttable 
    
# Test cases
solution = Solution()      

# Example test case 1
s="racecar"
t="carrace"
print(solution.isAnagram(s, t))

# Example test case 2
s="jar"
t="jam"
print(solution.isAnagram(s, t))