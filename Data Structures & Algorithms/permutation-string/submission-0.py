class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = {}
        window = {}

        # Frequency of s1
        for c in s1:
            count[c] = count.get(c, 0) + 1

        # First window
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1

        if window == count:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            # Add new character
            window[s2[r]] = window.get(s2[r], 0) + 1

            # Remove leftmost character
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]

            l += 1

            if window == count:
                return True

        return False
            