class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i==j:continue
                if nums[j]==0:
                    product = 0 
                    break
                product *= nums[j]
            arr.append(product)
        return arr

      
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length

        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]
        for i in range(length-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        answer = [left[i]*right[i] for i in range(length)]
        return answer