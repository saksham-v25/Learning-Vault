class Solution:
    def pivotIndex(self, nums):
        left=0
        right=0
        total_sum=0
        for i in range (len(nums)):
            total_sum+=nums[i]
        for i in range(len(nums)):
            if i==0:
                 left=0
                 right=total_sum-nums[i]-left
                
            else:

                left+=nums[i-1]
                right=total_sum-nums[i]-left
            if left==right:
                return i
        return -1
        