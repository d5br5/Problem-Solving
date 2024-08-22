class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)
        if slen > tlen : return False

        def isSub(si, ti):
            if si >= slen: return True
            if ti >= tlen: return False

            if s[si] == t[ti]: si+=1
            ti+=1
            return isSub(si, ti)
            
        return isSub(0, 0)
      
      
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        slen, tlen = len(s), len(t)
        si=ti=0

        while si < slen and ti < tlen:
            if s[si] == t[ti]: si+=1
            ti+=1
    
        return si == slen