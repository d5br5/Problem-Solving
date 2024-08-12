from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)
        if length<3 :return False
        
        minvalue = -(2**31)-1
        maxvalue = 2**31+1
        lmin = maxvalue
        rmax = minvalue
        l = []
        r = []
        for i in range(length):
            lmin = min(lmin, nums[i])
            l.append(lmin)
        for i in range(length-1, -1, -1):
            rmax = max(rmax, nums[i])
            r.append(rmax)
        for i in range(1, length-1):
            if l[i-1] < nums[i] and r[length-i-2] > nums[i]:return True
        return False
      
      

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False