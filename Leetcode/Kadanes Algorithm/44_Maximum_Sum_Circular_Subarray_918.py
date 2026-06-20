class Solution:
    def maxSubarraySumCircular(self, nums):
        def maxSum(nums):
            i=0
            bestending=nums[i]
            ans=nums[i]
            for i in range(1,len(nums)):
                v1=bestending+nums[i]
                v2=nums[i]
                bestending=max(v1,v2)
                ans=max(ans,bestending)
            return ans

        def minSum(nums):
            i=0
            bestending=nums[i]
            ans=nums[i]
            for i in range(1,len(nums)):
                v1=bestending+nums[i]
                v2=nums[i]
                bestending=min(v1,v2)
                ans=min(ans,bestending)

            sum=0

            for i in range (len(nums)):
                sum+=nums[i]
            if ans==sum:
                return ans
            else:
                total_sum=sum-ans
            return total_sum

        max_sum=maxSum(nums)
        min_sum=minSum(nums)

        circular_sum=max(max_sum,min_sum)
        return circular_sum        