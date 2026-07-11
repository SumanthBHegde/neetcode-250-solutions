class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                h = heights[stack.pop()]
                if stack:
                    l = stack[-1]
                else:
                    l = -1
                w = i-l-1
                maxArea = max(maxArea,h*w)                
            stack.append(i)
        return maxArea