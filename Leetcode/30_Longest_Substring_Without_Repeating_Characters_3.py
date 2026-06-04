class Solution:
    def lengthOfLongestSubstring(self, s):
        low=0
        high=0
        freq={}
        res=0

        for high in range(len(s)):
            char=s[high]
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1

            k=high-low+1

            while len(freq) < k:
                left_char=s[low]
                freq[left_char]-=1

                if freq[left_char]==0:
                    del freq[left_char]
                low+=1
                k=high-low+1

            res=max(res,high-low+1)

        return res
        
            
           