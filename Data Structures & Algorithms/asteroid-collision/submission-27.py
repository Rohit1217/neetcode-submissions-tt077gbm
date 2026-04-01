class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # We only care about collisions if stack top is moving RIGHT (+)
            # and current asteroid is moving LEFT (-)
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue # Current asteroid 'a' survives, check next stack element
                elif stack[-1] == -a:
                    stack.pop() # Both explode
                # If stack[-1] > -a, the current asteroid 'a' explodes
                break 
            else:
                # This 'else' belongs to the 'while' loop. 
                # It only runs if the while loop finished WITHOUT a 'break'.
                stack.append(a)
                
        return stack