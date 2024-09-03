# timeout
class Solution: 
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = -10000
        length = len(nums)
        for i in range(k, length+1):
            maximum = sum(nums[:i])
            newValue = maximum
            for j in range(i, length):
                newValue = newValue + nums[j] - nums[j-i]
                if maximum < newValue: maximum = newValue
            average = maximum / i
            if average > result : result = average
        return result