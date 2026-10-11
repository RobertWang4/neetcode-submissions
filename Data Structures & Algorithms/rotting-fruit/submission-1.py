from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        def rotten(i,j):
            nonlocal fresh
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return 
            grid[i][j] = 2
            fresh -= 1
            q.append((i,j))

        time = 0
        while q and fresh > 0:
            size = len(q)
            for i in range(size):
                r, c =q.popleft()
                rotten(r-1,c)
                rotten(r+1,c)
                rotten(r,c-1)
                rotten(r,c+1)
            time += 1
        return time if fresh == 0 else -1

                