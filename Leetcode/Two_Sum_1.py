from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        hashmap={}

        for i in range(n):
            x=target-nums[i]
            if x in hashmap :
                return [hashmap[x],i]

            hashmap[nums[i]]=i
        