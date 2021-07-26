from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Brute force, O(mn), O(1)
        # m, n = len(matrix), len(matrix[0])
        # length = m*n
        # rows, cols = set(), set()
        # row, col = 0, 0
        # spiral = [matrix[0][0]]
        
        # while len(spiral) < length:
        #     # Move right
        #     for j in range(col+1, n):
        #         spiral.append(matrix[row][j])
        #         if j+1 in cols or j+1 == n:
        #             col = j
        #             rows.add(row)
        #             break
            
        #     # Move down
        #     if len(spiral) == length:
        #         return spiral
            
        #     for i in range(row+1, m):
        #         spiral.append(matrix[i][col])
        #         if i+1 in rows or i+1 == m:
        #             row = i
        #             cols.add(col)
        #             break
            
        #     # Move left
        #     if len(spiral) == length:
        #         return spiral
            
        #     for j in range(col-1, -1, -1):
        #         spiral.append(matrix[row][j])
        #         if j-1 in cols or j-1 == -1:
        #             col = j
        #             rows.add(row)
        #             break
            
        #     # Move up
        #     if len(spiral) == length:
        #         return spiral
            
        #     for i in range(row-1, -1, -1):
        #         spiral.append(matrix[i][col])
        #         if i-1 in rows or i-1 == -1:
        #             row = i
        #             cols.add(col)
        #             break
        
        # return spiral


        # Simplify the above algorithm, O(mn), O(1)
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        spiral = []
        
        while top < bottom and left < right:
            # Move right
            for i in range(left, right):
                spiral.append(matrix[top][i])
            top += 1
            
            # Move down
            for i in range(top, bottom):
                spiral.append(matrix[i][right-1])
            right -= 1
            
            # Check conditions
            if top >= bottom or left >= right:
                break
    
            # Move left
            for i in range(right-1, left-1, -1):
                spiral.append(matrix[bottom-1][i])
            bottom -= 1
            
            # Move up
            for i in range(bottom-1, top-1, -1):
                spiral.append(matrix[i][left])
            left += 1
        
        return spiral
        

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.spiralOrder(matrix=[[1,2,3],[4,5,6],[7,8,9]]))
    print(solver.spiralOrder(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
