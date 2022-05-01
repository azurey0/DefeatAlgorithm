class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ## basically follows the description, O(N)
        self.lst = list(s)
        lens = len(self.lst)
        i = 0
        while i < lens:
            if lens - i < k:
                # fewer than k characters left, reverse all of them
                j = lens - 1
                self.reverse(i,j)
            elif (lens - i >= k) and (lens - i < 2*k):
                # less than 2k but >=  k characters, reverse the first k
                j = i + k - 1
                self.reverse(i,j)
                break 
            elif ( i%(2*k) == 0):
                # reverse first k
                j = i + k - 1
                self.reverse(i,j)            
            i += 2*k # jump every 2k element

        
        res = ''.join(self.lst)
        return res
        
    def reverse(self, i, j): # reverse list from index i to index j
        while i < j:
            self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
            i += 1
            j -= 1
        
        
