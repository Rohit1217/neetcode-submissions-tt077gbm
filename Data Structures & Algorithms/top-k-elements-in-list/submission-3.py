class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_list=[[] for num in nums]
        count_hash={}
        for num in nums:
            if num not in count_hash:
                count_hash[num]=1
            else:
                count_hash[num]+=1
        
        for num in count_hash:
            append_idx=count_hash[num]-1
            count_list[append_idx].append(num)

        res=[]
        for idx in range(len(nums)-1,-1,-1):
            for num in count_list[idx]:
                res.append(num)
                k=k-1
                if k==0:
                    return res

            
            


        