class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Given cars with arr position and speed.

        cars=list(zip(position,speed))
        cars.sort(reverse=True)

        times=[(target-pos)/speed for pos,speed in cars]

        if len(cars)==1:
            return 1
        
        # print(cars,times)
        num_fleet=1
        curr_max=times[0]

        for i in range(1,len(cars)):
            if times[i]>curr_max:
                num_fleet+=1
                curr_max=times[i]
        
        return num_fleet
        