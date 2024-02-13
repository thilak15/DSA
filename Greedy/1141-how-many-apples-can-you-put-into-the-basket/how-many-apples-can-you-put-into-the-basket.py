from typing import List

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        s = 0
        i = 0
        while i < len(weight):
            s += weight[i]
            if s > 5000:
                return i
            i += 1
        return i 
