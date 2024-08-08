import math 

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

class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        answer = ''
        l1 = len(str1)
        l2 = len(str2)
        l = min(l1,l2)

        i=1
        while i <= l:
            if (l1 % i == 0 and l2 % i == 0):
                m = str1[0:i]
                n = str2[0:i]
                if m==n:
                    if m*int(l1/i)==str1 and n*int(l2/i)==str2:
                        answer = m
                else:
                    return answer
            
            p=i
            q=int(l/i)
            while q > 1 :
                q = q-1
                if l % q == 0:
                    p = int(l/q)
                    break
                else:
                    p = math.ceil(l/q)

            if i < p :
                i = p
            else:
                break
        return answer
    
class Solution3:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1 :
            return ''
        l1 = len(str1)
        l2 = len(str2)

        gcdl = gcd(l1, l2)
        chunk = str1[:gcdl]

        return chunk if chunk*(l1//gcdl) == str1 and chunk*(l2//gcdl) == str2 else ''