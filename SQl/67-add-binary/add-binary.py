class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
    
        # Add the integers
        sum_int = int_a + int_b
    
        # Convert the sum back to a binary string
        result = bin(sum_int)[2:]
    
        return result


