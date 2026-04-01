class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        def sgn(x):
            if x>0:
                return 1
            else:
                return -1
        
        if len(asteroids)<2:
            return asteroids

        stack=[]
        flag=False

        for asteroid in asteroids:
            
            while len(stack)>0 and stack[-1]>0 and asteroid<0:

                if stack[-1]!=-asteroid:
                    if -asteroid>stack[-1]:
                        stack.pop()
                        stack.append(asteroid)
                else:
                    stack.pop()

                if len(stack)==0:
                    flag=True
                else:
                    asteroid=stack.pop() 

            if not flag:
                stack.append(asteroid)
            
            flag=False

        return stack
            