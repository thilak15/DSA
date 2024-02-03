class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True) 

        for i in range(1, len(nums) + 1):  # Start from 1 to len(nums)
            # Check if the current number of elements (i) is less than or equal to the current element
            # and if it is greater than the next element (if there is one)
            if i <= nums[i - 1] and (i == len(nums) or i > nums[i]):
                return i
        return -1
