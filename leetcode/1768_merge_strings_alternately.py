class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        minLength = min(len(word1), len(word2))
        for i in range(minLength):
            result = result + word1[i] + word2[i]
        return result + word1[minLength:] + word2[minLength:]
        