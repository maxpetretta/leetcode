class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Brute force, O(?)
        # def path(m, n, i, j):
        #     paths = 0
        #     if m == i and n == j:
        #         return 1
        #     if i < m:
        #         paths += path(m, n, i+1, j)
        #     if j < n:
        #         paths += path(m, n, i, j+1)
        #     return paths
        
        # return path(m-1, n-1, 0, 0)
        
        
        # Add memoization grid, O(mn), O(mn)
        # def path(m, n, i, j, memo):
        #     paths = 0
        #     if m == i and n == j:
        #         return 1
        #     elif memo[i][j] != 0:
        #         return memo[i][j]
        #     if i < m:
        #         paths += path(m, n, i+1, j, memo)
        #     if j < n:
        #         paths += path(m, n, i, j+1, memo)
            
        #     memo[i][j] = paths
        #     return paths
        
        # memo = [[0] * n for i in range(m)]
        # return path(m-1, n-1, 0, 0, memo)


        # Bottom up dynamic grid, O(mn), O(mn)
        # grid = [[1] * (n) for i in range(m)]
        
        # for i in range(1, m):
        #     for j in range(1, n):
        #         grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        # return grid[m-1][n-1]
    
    
        # Constant space bottom up, O(mn), O(min(m, n))
        if n > m:
            m, n = n, m
        col = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                col[j] += col[j-1]
    
        return col[n-1]
        

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.uniquePaths(m=3, n=7))
    print(solver.uniquePaths(m=3, n=2))
    print(solver.uniquePaths(m=7, n=3))
    print(solver.uniquePaths(m=3, n=3))
    print(solver.uniquePaths(m=23, n=12))
