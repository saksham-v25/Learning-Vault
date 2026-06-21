class Solution:
    def smallestSumSubarray(self, nums, n):

        bestending = nums[0]
        ans = nums[0]

        for i in range(1, n):
            v1 = bestending + nums[i]
            v2 = nums[i]

            bestending = min(v1, v2)
            ans = min(ans, bestending)

        return ans