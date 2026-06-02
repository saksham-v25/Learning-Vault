class Solution:
    from typing import List 

    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        n=len(arr)
        low=0
        high=0
        sum=0
        res=float('inf')

        while high<n:
            sum=sum+arr[high]

            while sum>=target:

                length=high-low+1
                res=min(res,length)
                sum=sum-arr[low]
                low=low+1

            high=high+1

        if res == float('inf'):
            return 0

        return res
