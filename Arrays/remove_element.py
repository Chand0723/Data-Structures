# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place
#  with O(1) extra memory.

'''
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]

'''

def remove_element(nums, val):
    temp = nums
    for i in range(0, len(temp)):
        if temp[i] == val:
            nums.pop(i)
        else:
            print('hello')

    return len(nums)

print(remove_element([3,2,2,3], 2))