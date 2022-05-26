# https://leetcode.com/problems/move-zeroes/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 记录有几个0， 就把非零的元素向前移动几位。因为排在前面的先移动，所以不会造成数值覆盖。
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1 
            else:
                nums[i - zeros] = nums[i]
        # 最后将末尾的n个0元素位置替换为0
        # 如果数组没有0，则不处理。
        if zeros > 0:
            nums[-zeros:] = [0] * zeros
        
