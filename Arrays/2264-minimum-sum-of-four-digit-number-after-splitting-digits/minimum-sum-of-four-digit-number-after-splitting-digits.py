class Solution:
    def minimumSum(self, num: int) -> int:
        digits=sorted([int(d) for d in str(num)])
        num1,num2=0,0

        for i,digit in enumerate(digits):
            if i%2==0:
                num1=num1*10 +digit
            else:
                num2=num2*10 +digit
        return num1+num2