class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        def get_sign(asteroid):
            return (asteroid>0)

        stack=[]
        i=1
        n=len(asteroids)

        for asteroid in asteroids:
            stack.append(asteroid)

            while len(stack)>1 and (get_sign(stack[-1])==False and get_sign(stack[-2])==True):
                asteroid1,asteroid2=stack.pop(),stack.pop()

                if abs(asteroid2)==abs(asteroid1):
                    continue
                
                elif abs(asteroid2)>abs(asteroid1):
                    stack.append(asteroid2)
                else:
                    stack.append(asteroid1)

        return stack
