#
# @lc app=leetcode.cn id=695 lang=python
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution(object):
    def dfs(self, grid, visited, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
             return 0
        visited[i][j] = True
        a = self.dfs(grid, visited, i+1, j, m, n)
        a += self.dfs(grid, visited, i-1, j, m, n)
        a += self.dfs(grid, visited, i, j+1, m, n)
        a += self.dfs(grid, visited, i, j-1, m, n)
        return a + 1
    def maxAreaOfIsland(self, grid):
        max_size = 0
        m,n = len(grid), len(grid[0])
        visited = [[ False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    size = self.dfs(grid, visited, i, j, m, n)
                    max_size = max(max_size, size)
        return max_size
# @lc code=end

# @km code=start
def dfs(grid, visited, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
             return 0
        visited[i][j] = True
        a = dfs(grid, visited, i+1, j, m, n)
        a += dfs(grid, visited, i-1, j, m, n)
        a += dfs(grid, visited, i, j+1, m, n)
        a += dfs(grid, visited, i, j-1, m, n)
        return a + 1
while True:
    try:
        params = list(map(int,input().split()))
        m,n = params[0],params[1]
        grid = [list(map(int,input().split())) for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        max_size = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    size = dfs(grid, visited, i, j, m, n)
                    max_size = max(max_size, size)
        print(max_size)
    except:
        break
# @km code=end