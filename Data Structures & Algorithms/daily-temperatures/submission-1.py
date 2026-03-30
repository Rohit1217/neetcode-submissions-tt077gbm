class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting_stack=[]
        result=[0]*len(temperatures)

        waiting_stack.append((0,temperatures[0]))
        for i in range(1,len(temperatures)):
            curr_max=waiting_stack[-1][1]
            if temperatures[i]>curr_max:
                while curr_max<temperatures[i] and len(waiting_stack)>0:
                    j,curr_max=waiting_stack.pop()
                    result[j]=i-j
                    if waiting_stack==[]:
                        curr_max=-1
                    else:
                        curr_max=waiting_stack[-1][1]
            waiting_stack.append((i,temperatures[i]))
        
        # for k in range(len(waiting_stack)):
        #     j,curr_max=waiting_stack.pop()
        #     result[j]=0
        
        return result

