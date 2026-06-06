class Solution:
    from typing import List 

    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        
        low=0
        high=0
        res = float('inf')
        sum=0

        for high in range(len(arr)):
            sum+=arr[high]

            while sum >= target:
                length=high-low+1
                res=min(res,length)
                sum-=arr[low]
                low+=1

        if res==float('inf'):
            return 0
        return res
