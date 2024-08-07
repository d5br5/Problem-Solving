# 공통길이까지 하나씩 번갈아가면서 합치고, 남은 문자열은 그대로 붙이기
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        minLength = min(len(word1), len(word2))
        for i in range(minLength):
            result = result + word1[i] + word2[i]
        return result + word1[minLength:] + word2[minLength:]

# 비슷한데, zip을 사용해서 한번에 처리
class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = []
        for (a,b) in zip(word1, word2):
            arr.append(a+b)
        arr.append(word1[len(word2):])
        arr.append(word2[len(word1):])
        return "".join(arr)