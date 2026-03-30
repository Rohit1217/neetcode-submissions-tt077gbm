class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles)>h:
            return 0

        right=max(piles)
        left=1
        res=1
        while left<right:
            mid=(left+right)//2
            time_taken=sum([((pile-1)//mid)+1 for pile in piles])
            
            if time_taken<=h:
                right=mid
                res=mid
            else:
                left=mid+1


        return right
        