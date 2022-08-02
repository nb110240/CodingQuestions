def numIslands(self, grid: List[List[str]]) -> int:
        #island is formed by land connected horizontaly or vertically 
        visit = set() 
        out = 0
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c = row+dr, col+dc
                    if (r in range(len(grid)) and 
                    c in range(len(grid[0])) and 
                    grid[r][c] =='1'and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visit:
                    bfs(i,j)
                    out +=1
        return out