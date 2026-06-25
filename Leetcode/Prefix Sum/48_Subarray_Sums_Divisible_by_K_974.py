class Solution:
    from typing import List
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        sum = 0
        f = {0 : 1}
        for i in range(n):
            sum += nums[i]
            rem = sum % k
            if rem < 0:
                rem = rem + k
            if rem in f:
                result = result + f[rem]
                f[rem] += 1
            else:
                f[rem] = 1

        return result
        