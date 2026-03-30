class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums=sum(nums)
        if sums%2!=0:
            return False
        else:
            target=sums//2

        self.memo=[-1 for _ in range(target+1)]
        
        def findsum_memo(target,num_list):
            if target==0:
                return True
            elif target<0:
                return False
            elif self.memo[target]!=-1:
                return self.memo[target]
            else:
                for i  in range(len(num_list)):
                    num=num_list[i]
                    print(num,target-num,target)
                    ans=findsum_memo(target-num,num_list[i+1:])
                    if ans==True:
                        self.memo[target]=True
                        return self.memo[target]
            self.memo[target]=False
            return self.memo[target]

        findsum_memo(target,nums)
        return self.memo[target]        