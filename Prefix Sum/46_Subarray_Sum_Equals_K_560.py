class Solution:
    from typing import List
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        hashmap = {0:1}
        result = 0
        for i in range(len(nums)):
            sum += nums[i]
            question = sum - k
            if question in hashmap:
                result +=hashmap[question]
            
            if sum in hashmap:
                hashmap[sum] += 1
            else:
                hashmap[sum]=1
        return result















        