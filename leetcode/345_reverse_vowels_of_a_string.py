class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowels(s):
            return 'aeiouAEIOU'.__contains__(s)
        
        arr = []
        answer = list(s)
        for i in range(len(answer)):
            if isVowels(answer[i]):
                arr.append(answer[i])
                answer[i] = None
        for i in range(len(s)):
            if answer[i] is None:
                answer[i] = arr.pop()
        return "".join(answer)
    
    
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        arr = list(s)
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and arr[left] not in vowels: left += 1
            while left < right and arr[right] not in vowels: right -= 1
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return "".join(arr)