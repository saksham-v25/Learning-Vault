class Solution:
    from typing import List
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        left=1
        right=1

        for i in range(1,n):
            
            left=left*nums[i-1]
            res[i]=left

        for i in range(n-1, -1, -1):
            res[i] = res[i] * right
            right = right * nums[i]

        return res

            
