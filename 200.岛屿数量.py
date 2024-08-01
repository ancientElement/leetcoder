#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def bfs(self,grid,visited, i, j, m, n):
        queue = []
        queue.append([i,j])
        while queue:
            i, j = queue.pop(0)
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == '0':
                continue
            visited[i][j] = True
            queue.append([i + 1, j])
            queue.append([i - 1, j])
            queue.append([i, j + 1])
            queue.append([i, j - 1])
    def dfs(self,grid,visited, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == '0':
            return
        visited[i][j] = True
        self.dfs(grid,visited, i + 1, j, m, n)
        self.dfs(grid,visited, i - 1, j, m, n)
        self.dfs(grid,visited, i, j + 1, m, n)
        self.dfs(grid,visited, i, j - 1, m, n)
    def numIslands(self, grid):
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.bfs(grid, visited, i, j, m, n)
                    count = count + 1
        return count

        
# @lc code=end

# @kc code=start
def dfs(grid,visited,i,j,m,n):
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
        return  
    visited[i][j] = True
    dfs(grid,visited,i+1,j,m,n)
    dfs(grid,visited,i-1,j,m,n)
    dfs(grid,visited,i,j+1,m,n)
    dfs(grid,visited,i,j-1,m,n)
    
def bfs(grid,visited,i,j,m,n):
    queue = []
    queue.append([i,j])
    visited[i][j] = True
    while len(queue) > 0:
        i,j = queue.pop(0)
        visited[i][j] = True
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
            continue  
        queue.append([i+1,j])
        queue.append([i-1,j])
        queue.append([i,j+1])
        queue.append([i,j-1])

while True:
    try:
        params = list(map(int,input().split()))
        m,n = params[0],params[1]
        grid = [map(int,input().split()) for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    dfs(grid,visited,i,j,m,n)
                    count = count + 1
        print(count)
    except FOEError:
        break
# @kc code=end