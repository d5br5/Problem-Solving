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
        from math import gcd
        return str1[:gcd(len(str1), len(str2))] 

class Solution4:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1 :
            return ''
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])
# solution 1
# 길이 1부터 짧은 길이까지 brute force
# valid? 길이가 나누어져야하고, 덩어리 반복했을때 원래 문자열이 나와야 함

# solution 3
# 반복되는 문자열이라면, str1+str2 하든 str2+str1 하든 같은 문자열이 나옴
# 반복 덩어리가 있다면, 그 문자열의 길이는 반드시 최대공약수와 같음
# 1. 최대공약수보다 작은 길이 덩어리가 있다면, 최대공약수 또한 그 수의 배수기 때문에 최대 길이가 아니게 됨
# 2. 최대공약수보다 긴 길이가 있다면, 그 수는 공약수가 아님. 
# 따라서 반복 문자열이라면, 무조건 덩어리는 최대공약수덩어리

# solution 4 : recursive 최고!!!!
# gcd를 찾지 않고, 짧은 문자열과 다른 문자열의 그 뒷부분을 재귀적으로 비교
