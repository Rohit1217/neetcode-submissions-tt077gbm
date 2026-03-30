class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles)>h:
            return 0

        right=max(piles)
        left=1

        while (right-left)>1:
            mid=(left+right)//2
            time_taken=sum([((pile-1)//mid)+1 for pile in piles])
            
            if time_taken<=h:
                right=mid
            else:
                left=mid
        if sum([((pile-1)//left)+1 for pile in piles])<=h:
            return left

        return right
        