from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # (start_index, height)

        for i, h in enumerate(heights):
            start = i
            # need to check stack is non-empty; also missing 'and' in your code
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stack.append((start, h))

        n = len(heights)
        # drain remaining bars
        for i, h in stack:
            maxArea = max(maxArea, h * (n - i))

        return maxArea
