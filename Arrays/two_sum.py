# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
'''

def two_sum(nums, target):
    first_num, second_num = 0,0
    target_array = []
    for i in range(len(nums)):
        first_num = nums[i]
        for j in range(i+1, len(nums)):
            second_num = nums[j]
            if first_num + second_num == target:
                target_array.append(i)
                target_array.append(j)
            
    return target_array


print(two_sum([2,7,11,15],9))