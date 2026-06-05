class Solution:
    def characterReplacement(self, s, k):

        low = 0
        freq = {}
        res = 0

        for high in range(len(s)):

            ch = s[high]

            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

            max_count = max(freq.values())

            while (high - low + 1) - max_count > k:

                left_char = s[low]

                freq[left_char] -= 1

                if freq[left_char] == 0:
                    del freq[left_char]

                low += 1

                max_count = max(freq.values())

            res = max(res, high - low + 1)

        return res