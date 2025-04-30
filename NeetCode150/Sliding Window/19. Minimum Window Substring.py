class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # find the shortest substring of s that includes all t 
        # we have:
            #1 left pointer, right pointer
            #2 countT table for the t str characters
            #3 window table for the current character condition 
            #4 a Need counter that is set still to the length of t 
            #5 a Have counter that will update as we shift out l, r pointer 
            #6 a res[] that keeps track of the current minimum window index 
            #6.1 a resLen to keep track of the length of the current result index 

        # base case when t is empty 
        if t == "": return ""
        # Set countT to record the character for t // the Need 
        # Set window to check the current character condition // the Have 
        countT, window = {}, {}

        # count the character in t and record to countT
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Set have and need. len(countT) gives us the number of unique character in t that we need 
        have, need = 0, len(countT)

        # Set res and resLen
        res, resLen = [-1, -1], float("infinity")
        
        # set left pointer 
        l = 0
        
        # right pointer will iterate through t and add the character count to the window
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            # check if the character is in counT, and if it is check if that character count has meet the need 
            if c in countT and window[c] == countT[c]:
                have += 1 
            
            # when have == need that means the current window has the result of what we want 
            while have == need:
                # it should at least run once if we ever get to this point 
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # shrinking from the left of the window
                # knowing that the removed character might not be the one we care about
                window[s[l]] -= 1 
                # thiws line is checking if the removed ones are the one we care, and we need to update have 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # no matter what we are incrementing the l and check the condition as long as have == need 
                l += 1 

        # l, r = res // Extracts the start and end indices of the best window
        # if resLen != float("infinity") // Ensures we return a result only if a valid window was found
        # s[l:r+1]	// Extracts the substring, making sure to include r
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
    
# Test cases
solution = Solution()

# Example test case 1
s="ADOBECODEBANC"
t="ABC"

print(solution.minWindow(s, t))