class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        c=0
        k=0
        for i in freq.values():
            if i%2==0:
                c+=i
            else:
                c+=(i-1)
                k=1
        return c+k