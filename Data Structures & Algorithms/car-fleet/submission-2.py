class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)==0:
            return 0
        combined=zip(position,speed)
        combined=sorted(combined)
        position,speed=zip(*combined)
        fleet=1
        curr_min_time=(target-position[-1])/speed[-1]
        for i in range(len(position)-1,-1,-1):

            curr_time=(target-position[i])/speed[i]
            print(curr_time,curr_min_time,i)
            if curr_time>curr_min_time:
                fleet+=1
                curr_min_time=curr_time
            
        return fleet

            