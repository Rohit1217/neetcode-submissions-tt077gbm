class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo=[-1 for i in range(len(nums)+1)]
        self.n=len(nums)
        def rob_memo(i):
            if i>self.n-1:
                return 0
            elif self.memo[i]!=-1:
                return self.memo[i]
            else:
                self.memo[i]=max(nums[i] + rob_memo(i+2),rob_memo(i+1))
                return self.memo[i]
        rob_memo(0),rob_memo(1)
        print(self.memo)
        return max(rob_memo(0),rob_memo(1))