class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sol_prefix_set = set()
        count=0

        for word in strs:
            word_prefix_set = set()
            prefix = ""
            count+=1
            
            for char in word:
                prefix += char
                word_prefix_set.add(prefix) 
            
            if count==1 :
                sol_prefix_set = word_prefix_set
            else:
                sol_prefix_set = sol_prefix_set & word_prefix_set
            
        # sol_prefix_list = list(sol_prefix_set)

        sol_prefix = ""
        prefix_len = 0
        

        for prefix in sol_prefix_set:    
            if len(prefix) >  prefix_len:
                sol_prefix = prefix
                prefix_len = len(prefix)

        return sol_prefix
        