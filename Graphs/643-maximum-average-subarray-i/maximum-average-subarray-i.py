class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Compute the sum of the first subarray of length k
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Use sliding window to find the maximum sum of any subarray of length k
        for i in range(k, len(nums)):
            # Slide the window: subtract the element going out and add the new element
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        # The maximum average is the maximum sum divided by k
        return max_sum / k
