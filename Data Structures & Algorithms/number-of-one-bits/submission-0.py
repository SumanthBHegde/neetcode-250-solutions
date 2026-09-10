class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in bin(n)[2:]:
            cnt += int(i)
            print(cnt)
        return cnt