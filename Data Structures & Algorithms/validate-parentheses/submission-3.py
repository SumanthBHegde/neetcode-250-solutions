class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            item = ""
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
                print
            elif not stack:
                return False
            else:
                item = stack.pop()
                item+=ch
                if item != "()" and item != "{}" and item != "[]":
                    return False
        return len(stack) == 0 