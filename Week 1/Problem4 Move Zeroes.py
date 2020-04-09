""" Move Zeroes
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Example:

    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Ahmed Ibrahim 
    """
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        st = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                while(st < i  and nums[st]!=0):
                    st+=1
                if st < i and st !=i:
                    tmp = nums[i]
                    nums[i] = nums[st]
                    nums[st] = tmp
        return nums
