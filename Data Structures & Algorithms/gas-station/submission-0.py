class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        num_used=0
        n=len(gas)

        start=0
        sums=0
        i=start

        count=0

        while num_used<n:
            sums+=gas[i]-cost[i]

            while sums<0 and num_used<n:
                start=(start-1)%n
                num_used+=1
                sums+=gas[start]-cost[start]

            i=(i+1)%n
            num_used+=1
        
        if sums<0:
            return -1
        
        return start