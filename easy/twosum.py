
def twoSum(nums, target):

    # for i in range(len(nums)):
    #     l = nums[i]
    #     for j in range(i+1,len(nums)):
    #         total = nums [i] + nums[j]
    #         if total == target:
    #             return(i,j)
    for i in range(len(nums)):
        ele = nums[i]
        diff = target - nums[i]
        if diff in nums[i + 1:]:
            return (i, 1 + i + nums[i + 1:].index(diff))


nums = [2,7,11,15]
target = 26
print(twoSum(nums,target))