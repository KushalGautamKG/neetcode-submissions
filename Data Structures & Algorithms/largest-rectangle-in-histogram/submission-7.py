class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        stack = [] # (index, heights[i])

        maxArea = 0

        for i, n in enumerate(heights):

            start = i


            while stack and stack[-1][1] > n:
                index, height = stack.pop()

                start = index


                maxArea = max(maxArea, height * (i - index))


            stack.append((start, n))



        for i, n in stack:
            maxArea = max(maxArea, (len(heights) - i) * n)


        return maxArea

