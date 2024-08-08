class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0 : return True
        
        if flowerbed[0] == 0 :
            flowerbed.insert(0, 0)
        if flowerbed[-1] == 0:
            flowerbed.append(0)
        
        chunk=0
        for i in flowerbed:
            if i==0: 
                chunk = chunk+1
            else: 
                if chunk > 0:
                    seat = (chunk-1)//2
                    n = n - seat
                    
                    if n<=0 : return True
                    chunk = 0

        seat = (chunk-1)//2
        n = n - seat
        return n<=0


