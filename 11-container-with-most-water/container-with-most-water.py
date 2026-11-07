class Solution:
    def maxArea(self, height: list[int]) -> int:

        area = 0
        l_pointer = 0
        r_pointer = len(height) - 1

        while l_pointer < r_pointer:

            current = min(height[l_pointer], height[r_pointer]) * (r_pointer - l_pointer)

            if current > area:
                area = current

            if (height[l_pointer] >= height[r_pointer]):
                r_pointer -= 1
            else:
                l_pointer += 1

        return area

        