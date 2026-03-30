class Solution:
    def climbStairs(self, n: int) -> int:
        self.num_steps_table={}

        def climbStairs_memo(n):
            if n<0:
                return 0
            elif n==1 or n==0:
                return 1
            if n in self.num_steps_table:
                return self.num_steps_table[n]
            else:
                self.num_steps_table[n]=climbStairs_memo(n-1)+climbStairs_memo(n-2)
            
            return self.num_steps_table[n]
    
        return climbStairs_memo(n)