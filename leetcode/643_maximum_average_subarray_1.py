class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = sum(nums[:k])
        length = len(nums)
        newValue = maximum
        for i in range(k, length):
            newValue = newValue + nums[i] - nums[i-k]
            if maximum < newValue : maximum = newValue
        return maximum / k

