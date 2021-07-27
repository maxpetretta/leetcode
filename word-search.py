from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Brute force with recursive backtracking, O(mn * 3^len(word)), O(len(word))
        # self.rows, self.cols = len(board), len(board[0])
        # self.board = board
        
        # for row in range(self.rows):
        #     for col in range(self.cols):
        #         if self.backtrack(row, col, word):
        #             return True
        # return False
    
    # def backtrack(self, row, col, word):
        
        # Base case, word has been found
        # if len(word) == 0:
        #     return True

        # # Check if inside boundaries
        # if row < 0 or row == self.rows or col < 0 or col == self.cols \
        #         or self.board[row][col] != word[0]:
        #     return False

        # # Mark current position
        # res = False
        # self.board[row][col] = "0"

        # # Check up/down/left/right for next letter
        # for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #     res = self.backtrack(row+i, col+j, word[1:])
        #     if res:
        #         break

        # self.board[row][col] = word[0]
        # return res


        # Simplify the above, O(mn * 3^len(word)), O(len(word))
        def backtrack(row, col, word):
            if len(word) == 0:
                return True
            
            if (row < 0 or row == rows or
                col < 0 or col == cols or
                board[row][col] != word[0] or (row, col) in seen):
                return False
            
            seen.add((row, col))
            res = (backtrack(row-1, col, word[1:]) or
                   backtrack(row+1, col, word[1:]) or
                   backtrack(row, col-1, word[1:]) or
                   backtrack(row, col+1, word[1:]))
            seen.remove((row, col))
            return res


        rows, cols = len(board), len(board[0])
        seen = set()

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, word): return True
        return False


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED"))
    print(solver.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="SEE"))
    print(solver.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCB"))
