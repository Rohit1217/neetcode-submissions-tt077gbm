class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        memo=[-1 for i in nums]
        prev=[-1 for i in nums]
        
        def lis_rec(i):
            if i>n-1:
                return 0
            elif memo[i]!=-1:
                return memo[i]
            else:
                maxm=1
                parent=i
                for idx in range(i):
                    if nums[idx]<nums[i]:
                        curr_maxm=max(maxm,1+lis_rec(idx))
                        
                        if curr_maxm>maxm:
                            maxm=curr_maxm
                            parent=idx
                
                memo[i]=maxm
                prev[i]=parent                

            return memo[i]

        for idx in range(n):
            lis_rec(idx)
        # max_index=0
        # maxm=0
        # for idx in range(n):
        #     if maxm<lis_rec(idx):
        #         max_index=idx
        #         maxm=lis_rec(idx)

        # seq=[]
        # while prev[max_index]!=max_index:
        #     seq=[nums[max_index]]+seq
        #     max_index=prev[max_index]
        
        # seq=[nums[max_index]]+seq


        
        # print(prev,memo,seq)

        return max(memo)