class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        len_n = len(nums)
        lis = [1] * len_n #记录每个位置上，它之前的最长递增序列的长度
        
        for i in range(len_n):
            for j in range(i):
              # 如果位置i上，她之前的位置j（1~i）的nums[j]<nums[i],寻找最长的lis[j],+1就是位置i上最长递增序列的长度。
                if nums[i] > nums[j] and lis[i] <= lis[j]:
                    lis[i] = lis[j] + 1
        return max(lis)
    
        
        
