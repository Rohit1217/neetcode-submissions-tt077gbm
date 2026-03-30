class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack=[]
        for operation in operations:
                
            if operation=="+":
                a,b=stack[-1],stack[-2]
                stack.append(a+b)

            elif operation=="D":
                stack.append(stack[-1]*2)
            
            elif operation=="C":
                stack.pop()
            else:
                stack.append(int(operation))
            print(stack)        

        return sum(stack)