""" Maximum Subarray
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    Ahmed Ibrahim 
    """
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ans = 0
        min_num = -1e18
        max_cur=0
        for i in nums:
            max_cur+=i
            max_ans = max(max_ans, max_cur)
            if max_cur < 0:
                max_cur=0
            min_num = max(min_num,i)
        if max_ans == 0:
            return min(max_ans, min_num)
        return max_ans
