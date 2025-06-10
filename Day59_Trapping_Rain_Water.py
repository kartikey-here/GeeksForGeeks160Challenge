#Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 


class Solution:
    def maxWater(self, height):
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
        return water_trapped
        # code here
