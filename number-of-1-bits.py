class Solution:
    def hammingWeight(self, n: int) -> int:
        # Count the number of 1 bits, O(1), O(1)
        # count = 0
        # mask = 1
        
        # for i in range(32):
        #     if n & mask != 0:
        #         count += 1
        #     mask <<= 1
        # return count
        
        
        # Use modulo operations, O(1), O(1)
        # count = 0
        # while n > 0:
        #     count += n % 2
        #     n >>= 1
        # return count

        
        # Skip over 0s and flip least-significant 1 bit, O(1), O(1)
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.hammingWeight(n=0))
    print(solver.hammingWeight(n=1))
    print(solver.hammingWeight(n=99999))
    print(solver.hammingWeight(n=4294967295))
