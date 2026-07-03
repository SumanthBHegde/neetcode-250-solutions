class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = "".join(c.lower() for c in s if c.isalnum())
        f,l = 0,len(test)-1
        while f<l:
            if test[f] != test[l]:
                return False
            f += 1
            l -= 1
        return True