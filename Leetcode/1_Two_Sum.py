class Solution(object):

    def twoSum(self, numbers, target):

        i = 0
        j = len(numbers) - 1

        while i < j:

            total = numbers[i] + numbers[j]

            if total == target:
                return [i + 1, j + 1]

            elif total > target:
                j -= 1

            else:
                i += 1


obj = Solution()

# Example 1
print(obj.twoSum([2,7,11,15], 9))

# Example 2
print(obj.twoSum([2,3,4], 6))

# Example 3
print(obj.twoSum([-1,0], -1))




# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.