class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=1,x//2

        while left<=right:
            guess=(left+right)//2
            if guess**2<x:
                left=guess+1
            elif guess**2==x:
                return guess
            else:
                right=guess-1
        
        if (left*left)>x:
            return left-1
        
        return left