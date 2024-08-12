class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        index = 0

        for i in range(1, len(chars)):
            if chars[i-1] == chars[i]:
                count += 1
            else:
                chars[index] = chars[i-1]
                index += 1

                if count != 1:
                    for digit in list(str(count)):
                        chars[index] = digit
                        index += 1 
                    count = 1
        
        chars[index] = chars[len(chars)-1]
        index += 1 
        if(count != 1): 
            for digit in list(str(count)):
                chars[index] = digit
                index += 1 
        
        return index
      
      
class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        index = 0
        length = len(chars)

        while index < length :
            letter = chars[index]
            count = 0
            while index <length and chars[index] == letter:
                count +=1
                index+=1
            
            chars[ans] = letter
            ans+=1
            if count > 1:
                for c in list(str(count)):
                    chars[ans] = c
                    ans +=1 
    
        return ans