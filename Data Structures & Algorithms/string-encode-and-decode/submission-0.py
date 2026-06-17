class Solution:

    def __init__(self):
        self.lengths = []

    def encode(self, strs: List[str]) -> str:
        res = ""
        self.lengths = []

        for s in strs:
            self.lengths.append(len(s))   # store length

            for c in s:
                temp = (ord(c) + 3) % 255
                res += chr(temp)

        return res

    def decode(self, s: str) -> List[str]:
        decoded = ""

        for c in s:
            temp = (ord(c) - 3) % 255
            decoded += chr(temp)

        res = []
        start = 0

        for length in self.lengths:
            res.append(decoded[start:start + length])
            start += length

        return res