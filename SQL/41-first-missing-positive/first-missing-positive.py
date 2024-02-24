class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash_table = {}
        for i, num in enumerate(nums):
            hash_table[num] = i
        for i in range(1, len(nums) + 2):
            if i not in hash_table:
                return i