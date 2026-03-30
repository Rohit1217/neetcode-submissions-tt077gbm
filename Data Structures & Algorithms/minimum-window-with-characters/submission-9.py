from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count_t=defaultdict(int)
        for char in t:
            char_count_t[char]+=1        

        start=0
        end=0
        n=len(s)
        n_t=len(char_count_t)


        satisfied=0
        
        res_start=0
        res_end=n
        res_len=n+1
        char_count_s=defaultdict(int)

        while end<n:
            char_count_s[s[end]]+=1
            
            if char_count_s[s[end]]==char_count_t[s[end]] and char_count_t[s[end]]!=0:
                satisfied+=1

            while(satisfied==n_t):
                if char_count_s[s[start]]==char_count_t[s[start]] and char_count_t[s[start]]!=0:
                    satisfied-=1
                char_count_s[s[start]]=max(0,char_count_s[s[start]]-1)
            
                if res_len>(end-start+1):
                    res_len=end-start+1
                    res_start=start
                    res_end=end

                start+=1

            end+=1
        print(res_start,res_end,res_len,n,s[res_start:res_end+1])
        if res_len<n+1:
            return s[res_start:res_end+1]

        return ""