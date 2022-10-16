class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Use bitwise operators to sum, O(1), O(1)
        # x, y = abs(a), abs(b)
        # sign = 1 if a > 0 else -1
        
        # # Flip the operands if y is greater
        # if x < y:
        #     return self.getSum(b, a)
        
        # # Sum positive ints
        # if a * b >= 0:
        #     while y != 0:
        #         answer = x ^ y
        #         carry = (x & y) << 1
        #         x, y = answer, carry
                
        # # Difference of ints
        # else:
        #     while y != 0:
        #         answer = x ^ y
        #         borrow = ((~x) & y) << 1
        #         x, y = answer, borrow
        
        # return sign * x


        # Use python-specific operations, O(1), O(1)
        mask = 0xFFFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)


if __name__ == "__main__":
    solver = Solution()
    print(solver.getSum(a=1, b=2))
    print(solver.getSum(a=2, b=3))
    print(solver.getSum(a=15, b=2))
    print(solver.getSum(a=5, b=-13))
