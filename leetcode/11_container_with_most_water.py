class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        area = 0

        while left < right :
            h_right = height[right]
            h_left = height[left]
            area = max(area, (right-left)*min(h_left, h_right))
            if h_left > h_right : right-=1
            else : left += 1

        return area
