class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        result = 0 
        for item in nums:
            if item in count: count[item]+=1
            else: count[item] = 1

        for key in count.keys():
            if key == k/2: 
                result += (count[key] // 2)
                continue
            if key > k/2: 
                continue
            if k-key in count:
                result += min(count[key], count[k-key])
                
        return result            

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0 
        for item in nums:
            complement = k - item
            if complement in hashmap and hashmap[complement] > 0:
                count +=1
                hashmap[complement] -= 1
            else:
                if item in hashmap: hashmap[item] +=1
                else : hashmap[item] = 1
        
        return count
      
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        left = 0
        right = len(nums)-1

        while left < right :
            addsum = nums[left] + nums[right]
            if addsum == k:
                count+= 1
                left+=1
                right-=1
            elif addsum < k: left+=1
            else: right -=1
        return count