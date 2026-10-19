class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                res = ''

                while stack and stack[-1] != '[':
                    res = stack.pop() + res

                stack.pop()  

                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * res)

        return ''.join(stack)