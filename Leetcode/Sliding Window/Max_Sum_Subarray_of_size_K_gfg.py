class Solution:
    def maxSubarraySum(self, a, k):
        n=len(a)
        low=0
        high=k-1
        sum=0
        res=0

        for i in range(0,k):
            sum=sum+a[i]
 
        while high<n:
            res=max(res,sum)
            low=low+1
            high=high+1

            if high==n:
                break
            sum=sum-a[low-1]
            sum=sum+a[high]

        return res 
    




    # class Solution:
    # def maxSubarraySum(self, arr, k):

    #     n = len(arr)

    #     window_sum = 0

    #     for i in range(k):
    #         window_sum += arr[i]

    #     res = window_sum

    #     low = 0
    #     high = k - 1

    #     while high < n:

    #         res = max(res, window_sum)

    #         low += 1
    #         high += 1

    #         if high == n:
    #             break

    #         window_sum = window_sum - arr[low - 1]
    #         window_sum = window_sum + arr[high]

    #     return res






        