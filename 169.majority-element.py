class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if counter == 0:
                candidate = nums[i]
                
            if nums[i] != candidate:
                counter -= 1
            else:
                counter += 1
            
        
        return candidate
