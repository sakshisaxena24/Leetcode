# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
# Example 1: Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]]
# Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#             nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#             nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2: Input: nums = [0,1,1] Output: []
# Explanation: The only possible triplet does not sum up to 0. Example 3:
# Input: nums = [0,0,0] Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
class Solution(object):
    def threeSum(self, nums):
        res = []  # empty list
        nums.sort()

        length = len(nums)

        for i in range(length - 2):
            # [0,0,0] and i should not be repeating
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = length - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l = l + 1
                elif total > 0:
                    r = r - 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
        return res




