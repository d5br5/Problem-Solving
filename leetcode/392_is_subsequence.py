class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)
        if slen > tlen : return False

        def isSub(si, ti):
            if si >= slen: return True

            sChar = s[si]
            for i in range(ti, tlen):
                if tlen-i < slen-si : return False
                if t[i] == sChar:
                    if isSub(si+1, i+1): return True

            return False    
            
        return isSub(0, 0)