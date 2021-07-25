from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Brute force, O(mn), O(mn)
        # def replace(matrix, x, y, touched):
            
        #     # Replace row
        #     for j in range(len(matrix[x])):
        #         if matrix[x][j] != 0:
        #             matrix[x][j] = 0
        #             touched[x][j] = True
            
        #     # Replace column
        #     for i in range(len(matrix)):
        #         if matrix[i][y] != 0:
        #             matrix[i][y] = 0
        #             touched[i][y] = True
            
        
        # m, n = len(matrix), len(matrix[0])
        # touched = [[False for y in range(n)] for x in range(m)]
        
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0 and not touched[i][j]:
        #             replace(matrix, i, j, touched)


        # Store the list of rows & cols to zero, O(mn), O(m + n)
        # m, n = len(matrix), len(matrix[0])
        # rows, cols = set(), set()
        
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        
        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0
        
        
        # Use first row/col as flags to save space, O(mn), O(1)
        m, n = len(matrix), len(matrix[0])
        firstCol = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
    
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.setZeroes(matrix=[[1,1,1],[1,0,1],[1,1,1]]))
    print(solver.setZeroes(matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
    print(solver.setZeroes(matrix=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]))
