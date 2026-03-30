class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)

        merged_length=max(m,n)

        ptr1=0
        ptr2=0

        res_list=[]
        for idx in range(merged_length):
            if idx<n:
                res_list.append(word1[idx])
            if idx<m:
                res_list.append(word2[idx])
        
        res_s=("").join(res_list)

        return res_s
