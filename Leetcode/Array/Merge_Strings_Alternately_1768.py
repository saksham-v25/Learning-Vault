class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merg = ""

        while i < len(word1) and i < len(word2):
            merg += word1[i] + word2[i]
            i += 1

        merg += word2[i:]

        merg += word1[i:]

        return merg
