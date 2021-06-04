class Solution:
    def reverseBits(self, n: int) -> int:
        # Brute force, O(1)
        # answer = 0
        # mask = 1
        # for i in range(32):
        #     if n & mask == 0:
        #         answer <<= 1
        #     else:
        #         answer = (answer << 1) + 1
        #     mask <<= 1
        # return answer
        
        
        # Reverse byte by byte, remembering results, O(1)
        def reverseByte(byte, cache):
            answer, mask = 0, 1
            if byte not in cache:
                for i in range(8):
                    if byte & mask == 0:
                        answer <<= 1
                    else:
                        answer = (answer << 1) + 1
                    mask <<= 1
                cache[byte] = answer
                return answer
            else:
                return cache[byte]
        
        answer, place = 0, 24
        cache = {}
        while n:
            answer += reverseByte(n & 0xff, cache) << place
            n = n >> 8
            place -= 8
        return answer
        
        
# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.reverseBits(n=43261596))
    print(solver.reverseBits(n=4294967293))
