class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sizeS, sizeT = len(s), len(t)
        if sizeS < sizeT:
            return ""
        countT,countS = {},{}
        for i in range(sizeT):
            countT[t[i]] = countT.get(t[i],0)+1
        resl = float('inf')
        res = [0,0]
        l = 0
        need = len(countT)
        have = 0
        for r in range(sizeS):
            
            countS[s[r]] = countS.get(s[r],0) + 1
            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have += 1
            
            while have == need:
                windowLen = r - l +1
                if windowLen < resl:
                    resl = windowLen
                    res = [l,r+1]
            
                if s[l] in countT and countT[s[l]] == countS[s[l]]:
                    have -= 1
                countS[s[l]] -= 1
                l += 1
            
        return s[res[0]:res[1]]
                