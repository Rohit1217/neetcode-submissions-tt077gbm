class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo=[-1 for i in range(len(cost)+1)]
        self.n=len(cost)
        def min_cost_climb_memo(i):
            if self.memo[i]!=-1:
                return self.memo[i]
            elif i==self.n:
                return 0
            elif i==self.n-1:
                return cost[self.n-1]
            elif  i==self.n-2:
                return cost[self.n-2]
            else:
                self.memo[i]= cost[i]+min(min_cost_climb_memo(i+1),min_cost_climb_memo(i+2))
                return self.memo[i]
        return min(min_cost_climb_memo(0),min_cost_climb_memo(1))
            
        