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

class Solution3:
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        point = max(m, n)
        i = 0
        result = []

        while i < point:
            if i < m:
                result += word1[i]
            if i < n:
                result += word2[i]
            i += 1

        return "".join(result)
      
# 두 문자열의 시작부터 끝까지 순회
# 기준을 2가지로 잡을 수 있음
# 1.두 길이 중 긴 길이
#   max 까지 병렬 순회. 각 문자열의 길이를 넘지 않았다면 answer에 추가
# 2. 두 길이 중 짧은 길이
#  중간까지 병렬 순회. 나머지 덩어리 한번에 붙이기