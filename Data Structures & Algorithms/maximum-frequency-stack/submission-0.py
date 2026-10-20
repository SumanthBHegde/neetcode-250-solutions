class FreqStack:

    def __init__(self):
        self.stack = {}
        self.group = {}
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.stack[val] = self.stack.get(val,0)+1
        f = self.stack[val]

        if f > self.maxfreq:
            self.maxfreq = f
        if f not in self.group:
            self.group[f] = []

        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.maxfreq].pop()
        self.stack[val] -= 1

        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()