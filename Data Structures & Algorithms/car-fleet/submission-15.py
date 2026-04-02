class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet_stack=[]
        pos_speed=list(zip(position,speed))
        pos_speed.sort(reverse=True)

        # print(pos_speed)
        for idx in range(len(pos_speed)):
            time_to_reach=max(0,(target-pos_speed[idx][0])/pos_speed[idx][1])

            if fleet_stack and fleet_stack[-1]>=time_to_reach:
                time_to_reach=fleet_stack[-1]
                fleet_stack.pop()
            
            fleet_stack.append(time_to_reach)

        return len(fleet_stack)
            
