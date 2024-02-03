class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs="".join(c.lower() for c in s if c.isalnum())
        i=0
        j=len(strs)-1

        while i<=j:
            if strs[i]==strs[j]:
                i+=1
                j-=1
            else:
                return False
        return True
