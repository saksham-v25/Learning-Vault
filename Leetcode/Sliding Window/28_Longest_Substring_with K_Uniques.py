class Solution:
    def longestSubstringKDistinct(self, s,k):
        low=0
        high=0
        freq={}
        res=-1

        for high in range(len(s)):
            ch=s[high]

            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1


            while len(freq) > k:
                left_char=s[low]
                freq[left_char]-=1

                if freq[left_char]==0:
                    del freq[left_char]

                low+=1

            if len(freq) == k:
                res=max(res,high-low+1)

        return res
       