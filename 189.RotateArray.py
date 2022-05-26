## Reverse list separately
#https://leetcode.com/problems/rotate-array/
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        # if k > len(nums), take % to reduce to 1 round result
        k = k % len(nums)
        # get last n elements
        l = nums[-k:]
        # move elements in list to the back
        for ele in range(len(nums) - 1, k-1, -1):
            nums[ele] = nums[ele - k]
        #print(nums)
        for ele in range(k):
            nums[ele] = l[ele]
        
        #print(nums)
        '''
        #原地赋值需要[:]这样哦
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        print(nums)
        
        return nums
        
        
