Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

class Solution(object):
    def moveZeroes(self, nums):
        
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                count += 1

# two pointers method
def movezero(nums):
    slow = fast = 0
    while fast < len(nums):
        if nums[slow] == 0 and nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # wait while we find a non-zero element to
        # switch with you
        if nums[slow] != 0:
            slow += 1

        # keep going
        fast += 1
                
