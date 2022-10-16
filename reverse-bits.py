class Solution:
    def reverseBits(self, n: int) -> int:
        # Brute force with iteration, O(1), O(1)
        # answer, mask = 0, 1
        # for i in range(32):
        #     if n & mask == 0:
        #         answer <<= 1
        #     else:
        #         answer = (answer << 1) + 1
        #     mask <<= 1
        # return answer
        
        
        # Reverse byte by byte, with memoization, O(1), O(1)
        def reverseByte(byte, memo):
            answer, mask = 0, 1
            if byte not in memo:
                for i in range(8):
                    if byte & mask == 0:
                        answer <<= 1
                    else:
                        answer = (answer << 1) + 1
                    mask <<= 1
                memo[byte] = answer
                return answer
            else:
                return memo[byte]
        
        answer, power = 0, 24
        memo = {}
        while n:
            answer += reverseByte(n & 0xff, memo) << power
            n = n >> 8
            power -= 8
        return answer
        
        
# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.reverseBits(n=43261596))
    print(solver.reverseBits(n=4294967293))
