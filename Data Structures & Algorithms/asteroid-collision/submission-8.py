class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        def sgn(x):
            if x>0:
                return 1
            else:
                return -1
        
        if len(asteroids)<2:
            return asteroids

        stack=[asteroids[0]]
        next_idx=1

        while next_idx<len(asteroids):
            val=asteroids[next_idx]
            stack.append(val)
            
            while len(stack)>1 and sgn(stack[-2])==1 and sgn(stack[-1])==-1:

                if stack[-2]!=-stack[-1]:
                    if abs(stack[-2])>abs(stack[-1]):
                        stack.pop()
                    else:
                        a,b=stack.pop(),stack.pop()
                        stack.append(a)    

                else:
                    stack.pop(),stack.pop()   

            next_idx+=1

        return stack
            