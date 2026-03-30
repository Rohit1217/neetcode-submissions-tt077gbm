class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo=[-1 for i in range(len(nums)+1)]
        self.n=len(nums)
        if self.n<4:
            return max(nums)
        def rob_memo(i):
            if i>self.n-1:
                return 0
            elif self.memo[i]!=-1:
                return self.memo[i]
            else:
                self.memo[i]=max(nums[i] + rob_memo(i+2),rob_memo(i+1))
                return self.memo[i]
        num_copy=nums[:]
        last_house=nums[-1]
        first_house=nums[0]
        second_house=nums[1]
        last_second_house=nums[-2]
        nums=nums[2:-1]
        self.n=len(nums)
        output1= rob_memo(0)+first_house
        
        self.memo=[-1 for i in range(len(nums)+1)]
        nums=[second_house]+nums[:-1]
        self.n=len(nums)
        output2= rob_memo(0)+last_house

        # self.memo=[-1 for i in range(len(nums)+1)]
        # nums=num_copy[1:-1]
        # self.n=len(nums)
        # output3= rob_memo(0)
        # print(output1,output2,output3,nums)

        return max(output1,output2)
        