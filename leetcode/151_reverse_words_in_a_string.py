class Solution:
    def reverseWords(self, s: str) -> str:
        chunk=''
        arr = []
        for i in s:
            if i==' ':
                if chunk!="":
                    arr.append(chunk)
                    chunk=''
            else:
                chunk += i
        if chunk != "":
            arr.append(chunk)
        arr.reverse()
        return ' '.join(arr)

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))