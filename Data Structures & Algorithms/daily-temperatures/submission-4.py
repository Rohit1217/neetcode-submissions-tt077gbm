class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        result=[0 for i in range(n)]

        for i in range(n):
            if stack:
                while stack and stack[-1][-1]<temperatures[i]:
                    j,temp=stack.pop()
                    result[j]=i-j
            
            stack.append((i,temperatures[i]))
        
        return result