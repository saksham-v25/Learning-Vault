class Solution:
    from typing import List
    def isSubsequence(self, s: str, t: str) -> bool:
        arr_s=list(s)
        arr_t = list(t)
        j=max(arr_s,arr_t)
        m=0
        n=0
        while m < len(arr_s) and n < len(arr_t):
            if arr_s[m] == arr_t[n]:
                m += 1
                n += 1
            
            else:
                n += 1
        if m == len(arr_s):
            return True
        else:
            return False
