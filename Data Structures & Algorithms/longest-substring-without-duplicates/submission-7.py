class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_loc={}
        if len(s)==0:
            return 0
        curr_max=1
        i=0
        j=1
        last_loc[s[0]]=0
        while j<len(s):            
            try:
                last_loc_char=last_loc[s[j]]
            except Exception as e:
                last_loc_char=-1

            
            if last_loc_char>=i:
                i=last_loc[s[j]]+1
            last_loc[s[j]]=j   

            print(last_loc,i,j)

            if j-i+1>curr_max:
                curr_max=j-i+1

            j+=1



        return curr_max
        