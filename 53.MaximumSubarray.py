class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curmax = nums[0]
        globalmax =  nums[0]
        for i in range(1, len(nums)):
            curmax = max(curmax+nums[i], nums[i])
            if curmax > globalmax:
                globalmax = curmax
        
        return globalmax
        # dynamic programming
        # compute max subarray for each position
        # the max subarray is the current value or current val + previous max subarray
