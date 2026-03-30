from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count_t=defaultdict(int)
        for char in t:
            char_count_t[char]+=1        

        start=0
        end=0
        n=len(s)


        def is_equal(count_s,count_t):
            for char in count_t:
                if count_s[char]<count_t[char]:
                    return False
            return True


        res_start=0
        res_end=n
        res_len=n+1
        char_count_s=defaultdict(int)

        while end<n:
            char_count_s[s[end]]+=1
            print(start,end)
            while(is_equal(char_count_s,char_count_t)):
                char_count_s[s[start]]=max(0,char_count_s[s[start]]-1)
                
            
                if res_len>(end-start+1):
                    res_len=end-start+1
                    res_start=start
                    res_end=end

                start+=1

            end+=1
        
        if res_len<n+1:
            return s[res_start:res_end+1]

        return ""