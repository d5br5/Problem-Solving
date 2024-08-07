class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        answer = ''
        m=len(str1)
        n=len(str2)
        length = min(m,n)
        for i in range(length):
            if(str1[i]!=str2[i]):
                return answer
            if(m%(i+1)!=0 or n%(i+1)!=0):
                continue
            chunk=str1[0:i+1]
            a=int(m/(i+1))
            b=int(n/(i+1))
        
            if(chunk*a==str1 and chunk*b==str2):
                answer=chunk
        return answer
