class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) <= 8:
            return len(word)
        else:
            full_chunks = len(word) // 8
            remaining_chars = len(word) % 8
            i=1
            s=0
            while i<=full_chunks:
                s+=(8*i)
                i+=1
            s+=(remaining_chars)*i
        return s
