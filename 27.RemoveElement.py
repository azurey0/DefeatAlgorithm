class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
    
        #双指针法：
        # 当前为需要删除的元素时，快指针走，慢不动
        # 当前为其他元素时，用快指针的值替换慢指针，从而用删除元素之后的数组替换，实现删除。之后慢指针+1
        # https://leetcode.com/problems/remove-element/
        
