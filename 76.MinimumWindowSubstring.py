## https://leetcode.com/problems/minimum-window-substring/

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        
        t_cnt = Counter(t)
        needs = len(t)
        res = []
        left = 0 
        min_len = 100000
        start, end = 0, -1 ### end needs to be -1 !!!!
        for right in range(len(s)):
            
            ## if right in t and has needs, needs - 1
            if s[right] in t_cnt:
                if t_cnt[s[right]] > 0:
                    needs -= 1
                t_cnt[s[right]] -= 1
                
            ## when right goes to the most end, move left till needs > 0
            while needs == 0:
                if right - left + 1 < min_len:# record length
                    min_len = right - left + 1
                    start, end = left, right
                    
                if s[left] in t_cnt:
                    if t_cnt[s[left]] >= 0:
                        needs += 1
                    t_cnt[s[left]] += 1
                    
                left += 1

        return s[start:end+1]

    
        
