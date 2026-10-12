from collections import deque
class Solution: 
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS, COLS = len(grid),len(grid[0])
        q = deque([])
        visit = [[False]*COLS for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit[i][j] = True
        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in direction:
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        not visit[nr][nc] and
                        grid[nr][nc] !=-1):
                        grid[nr][nc] = dist
                        visit[nr][nc] = True
                        q.append((nr,nc))
            

