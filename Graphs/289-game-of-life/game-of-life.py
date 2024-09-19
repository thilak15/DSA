class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def count_live_neighbours(i:int, j:int)->int:

            directions = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]

            live_neighbours = 0

            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < rows and 0 <= nj < cols and abs(board[ni][nj]) == 1:
                    live_neighbours +=1
            return live_neighbours

        # Count no of live neighbours for each cell
        for i in range(rows):
            for j in range(cols):
                live_neighbours = count_live_neighbours(i, j)

                if board[i][j] == 1:
                    if live_neighbours < 2 or live_neighbours > 3:
                        board[i][j] = -1  # cell is going to die
                else:
                    if live_neighbours == 3:
                        board[i][j] = 2  # cell is becoming alive

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0  # Died
                elif board[i][j] == 2:
                    board[i][j] = 1  # Became alive
