class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n<1:
            return -1

        prev_next=1
        prev=2

        for idx in range(n-3,-1,-1):
            temp=prev
            prev=prev_next+prev
            prev_next=temp
        
        return prev