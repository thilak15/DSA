from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0

        def rotten(r, c):
            nonlocal fresh
            if (
                0 <= r < len(grid)  # Check if row is within bounds
                and 0 <= c < len(grid[0])  # Check if column is within bounds
                and grid[r][c] == 1  # Check if the orange is fresh
            ):
                grid[r][c] = 2  # Mark the orange as rotten
                q.append((r, c))  # Add the position to the queue
                fresh -= 1  # Decrease the count of fresh oranges

        # Initialize the queue and count fresh oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # Perform BFS to rot adjacent fresh oranges
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                # Rot the adjacent oranges
                rotten(r + 1, c)
                rotten(r - 1, c)
                rotten(r, c + 1)
                rotten(r, c - 1)
            time += 1

        # If there are no fresh oranges left, return the time taken, else return -1
        return time if fresh == 0 else -1
