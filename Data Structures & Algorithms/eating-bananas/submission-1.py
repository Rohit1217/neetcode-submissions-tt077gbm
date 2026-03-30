class Solution:

    def find_time(self,piles,k,h):
        sum_time=0
        for pile in piles:
            sum_time+=pile//k+((pile%k)+k-1)//k
        if sum_time>h:
            return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)+1
        left=1
        while (right-left)>1:
            search_idx=(left+right)//2
            val=self.find_time(piles,search_idx,h)
            # val_left=find_time(search_idx-1)
            val_left=self.find_time(piles,search_idx-1,h)
            if  val and not val_left:
                return search_idx
            elif not val:
                left=search_idx+1
            else:
                right=search_idx
        
        return left
        




        

        