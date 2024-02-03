class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach=0
        for i,num in enumerate(nums):
            if i>max_reach:
                return 0
            max_reach=max(max_reach,i+num)

            if max_reach>=len(nums)-1:
                return True
        return False
