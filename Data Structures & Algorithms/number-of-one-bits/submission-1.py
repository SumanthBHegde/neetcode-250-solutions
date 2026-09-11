class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        # for i in bin(n)[2:]:
        #     cnt += int(i)
        #     print(cnt)
        while n:
            n = n & (n-1)
            cnt += 1
        return cnt