class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        if not matrix or not matrix[0]:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from left to right across the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move down the top boundary

            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move left the right boundary

            if top <= bottom:
                # Traverse from right to left across the bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move up the bottom boundary

            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move right the left boundary

        return result
