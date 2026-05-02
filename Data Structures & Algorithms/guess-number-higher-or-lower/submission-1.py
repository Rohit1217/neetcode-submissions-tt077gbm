# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=0
        right=n
        curr_guess=(left+right)//2
        
        while left<right:
            curr_guess=(left+right)//2
            if guess(curr_guess)==0:
                return curr_guess
            elif guess(curr_guess)==-1:
                right=curr_guess-1
            elif guess(curr_guess)==1:
                left=curr_guess+1

        return left