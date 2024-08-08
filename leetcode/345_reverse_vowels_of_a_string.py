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