class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        lst = s.split(' ')
        res = [x for x in lst if x != '']
        return ' '.join(res[::-1])
        '''
        ss = self.trim_start_space(s) # trim start
        ss = self.trim_start_space(ss[::-1]) # trim end
        ## ss is reversed.
        l, r = 0, 0
        while r < len(ss):
            if ss[r] == ' ':
                if ss[r + 1] == ' ': # if will not exceed because we trim end and start 
                    ss = ss[:r] + ss[r+1:] # delete 1 extra whitespace one at a time
                else: # reverse one word using 2 pointers.
                    ss = ss[:l] + ss[l:r][::-1] + ss[r:] #l, r are the start and end(whitespace) of current word. reverse it and keep the rest.
                    
                    r += 1
                    l = r
            else:
                r += 1
        
        ss = ss[:l] + ss[l:][::-1] # the last word is not processed. the l pointer is the place for the last word, after the while lool
        #print(ss, len(ss))
        return ss
                        
                    
    def trim_start_space(self, s):
        p = 0
        while s[p] == ' ' and p < len(s):
            p += 1
        return s[p:]

        
        
        
