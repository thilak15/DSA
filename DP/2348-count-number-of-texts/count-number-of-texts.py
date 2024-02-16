class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10**9 + 7
        dp = [0] * (len(pressedKeys) + 1)
        dp[0] = 1  # base case: there's one way to decode an empty string
    
        for i in range(1, len(pressedKeys) + 1):
            dp[i] = dp[i - 1]  # At least, the current digit can be decoded as itself
            # Check for 2-digit combination if it's the same digit
            if i > 1 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                dp[i] += dp[i - 2]
                dp[i] %= mod
                # Check for 3-digit combination
                if i > 2 and pressedKeys[i - 1] == pressedKeys[i - 3]:
                    dp[i] += dp[i - 3]
                    dp[i] %= mod
                    # Check for 4-digit combination for keys '7' and '9' only
                    if i > 3 and pressedKeys[i - 1] == pressedKeys[i - 4] and (pressedKeys[i - 1] == '7' or pressedKeys[i - 1] == '9'):
                        dp[i] += dp[i - 4]
                        dp[i] %= mod
    
        return dp[-1]

        