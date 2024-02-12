class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
       nums_filtered = sorted(set(nums) - {0})
       return len(nums_filtered)
            


