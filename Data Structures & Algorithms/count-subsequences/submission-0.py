class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        

        n=len(s)
        m=len(t)

        subseq=[0]*n

        for i in range(n):
            if s[i]==t[0]:
                subseq[i]=1

        for i in range(1,m):
            curr_val=t[i]
            newsubseq=[0]*n
            prefix_sum=0
            prefix_arr=[0]*n

            for j in range(0,n):
                prefix_sum=prefix_sum+subseq[j]
                prefix_arr[j]=prefix_sum

            for j in range(1,n):
                if s[j]==curr_val and j!=0:
                    newsubseq[j]=prefix_arr[j-1]
            
            subseq=newsubseq

        return sum(subseq)



