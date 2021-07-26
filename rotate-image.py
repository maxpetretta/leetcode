from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Brute force w/ second matrix, O(n^2), O(n^2)
        # n = len(matrix)
        # rotated = [[0 for i in range(n)] for i in range(n)]
        
        # for i in range(n):
        #     for j in range(n):
        #         rotated[i][j] = matrix[n-j-1][i]
        
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = rotated[i][j]


        # Rotate each layer in groups of four, O(n^2), O(1)
        # n = len(matrix)
        # l, r = 0, n-1
        
        # while l < r:
        #     for i in range(r - l):
        #         t, b = l, r
        #         temp = matrix[t][l+i]           # Save temp
        #         matrix[t][l+i] = matrix[b-i][l] # Top left
        #         matrix[b-i][l] = matrix[b][r-i] # Bottom left
        #         matrix[b][r-i] = matrix[t+i][r] # Bottom right
        #         matrix[t+i][r] = temp           # Top right
        #     l += 1
        #     r -= 1


        # Use matrix transpose & reflect from linear algebra, O(n^2), O(1)
        def transpose(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i, n):
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        def reflect(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
        
        transpose(matrix)
        reflect(matrix)


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.rotate(matrix=[[1,2,3],[4,5,6],[7,8,9]]))
    print(solver.rotate(matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
    print(solver.rotate(matrix=[[1]]))
    print(solver.rotate(matrix=[[1,2],[3,4]]))
