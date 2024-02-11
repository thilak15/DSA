class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # List to store factors of n
        factors = []
        
        # Find all factors of n
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
                
        # Check if we have enough factors
        if k <= len(factors):
            return factors[k - 1]  # Return the k-th factor, adjusting for 0-based indexing
        else:
            return -1  # Not enough factors