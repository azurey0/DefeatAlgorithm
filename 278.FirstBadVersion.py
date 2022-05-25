https://leetcode.com/problems/first-bad-version/
  #same idea to https://leetcode.com/problems/search-insert-position/
 # The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # print(isBadVersion(0)) default 0 is good
        low = 0
        high = n
        while low <= high:
            mid = (low + high)//2
            if isBadVersion(mid) == True and isBadVersion(mid - 1) == False:
                return mid
            elif isBadVersion(mid) == True:
                high = mid - 1
            else:
                low = mid + 1
            
