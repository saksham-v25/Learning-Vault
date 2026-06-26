class Solution:
    from typing import List
    def findMaxLength(self, nums: List[int]) -> int:
        zero=0
        one=0
        f={0:-1}
        res=0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1
            diff = zero -one
            if diff in f:
                idx = f[diff]
                length = i - idx
                res = max (length,res)
            else:
                f[diff] = i
        return res
        