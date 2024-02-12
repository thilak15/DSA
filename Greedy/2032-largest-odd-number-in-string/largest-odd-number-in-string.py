class Solution:
    def largestOddNumber(self, num: str) -> str:
        """i=0
        k=0
        c=0
        while i <len(num):
            if int(num[i])%2!=0:
                k=i
                c+=1
            i+=1
        if c>0:
            return num[:k+1]
        else:
            return """""
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""
        # Time Complexity O(n)
        # Space Complexity O(1)
