from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # assign the array to variable for easy use
        A, B = nums1, nums2
        total = len(A) + len(B)
        # the point where the grouped array is split into left and right portion 
        half = total // 2 
        
        # also want to make sure that A is the shorter one for computation
        if len(B) < len (A):
            A, B = B, A
        
        l, r = 0, len(A) - 1 
        while True:
            midA = (l + r) // 2 
            # remember that together for the left portion of A and B they make up the left part of the grouped array
            # so after arrangement midB is just half - midA
            # -2 is for the fact that midA and midB are index, so they start by 0 and we need to adjust that 
            midB = half - midA - 2 

            # index of the "end" of left part of A
            Aleft = A[midA] if midA >= 0 else float("-infinity")
            # index of the "start" of right part of A
            Aright = A[midA + 1] if (midA + 1) < len(A) else float("infinity")
            # index of the "end" of left part of B          
            Bleft = B[midB] if midB >= 0 else float("-infinity")
            # index of the "start" of right part of B
            Bright = B[midB + 1] if (midB + 1) < len(B) else float("infinity")
            
            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd length of combined array
                if total % 2:
                    return (min(Aright, Bright))
                # even length of combined array
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 
            
            # partition is not correct
            # left portion of A is too large, shrink
            elif Aleft > Bright:
                r = midA - 1 
            # left potion of A is too smal, extend
            else: 
                l = midA + 1 



        