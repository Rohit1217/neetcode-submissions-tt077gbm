class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)

        ptr1=0
        ptr2=0

        res_s=""

        while (ptr1<n) or (ptr2<m) :

            if ptr1<=ptr2 and ptr1!=n:                    
                res_s+=word1[ptr1]
                ptr1+=1
            
            elif ptr2!=m:
                res_s+=word2[ptr2]
                ptr2+=1
            
            else:
                res_s+=word1[ptr1]
                ptr1+=1

        return res_s
