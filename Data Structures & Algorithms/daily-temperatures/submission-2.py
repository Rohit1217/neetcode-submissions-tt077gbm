class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack=[]
        results=[0]*len(temperatures)
        idx=0

        for temp in temperatures:
            
            while monotonic_stack and temp>monotonic_stack[-1][0]:
                _,pos=monotonic_stack.pop()
                results[pos]=idx-pos
                # print("K",pos,idx)
            
            monotonic_stack.append((temp,idx))
            idx+=1

        return results
