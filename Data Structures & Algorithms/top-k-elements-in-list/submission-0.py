class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr=[[] for i in range(len(nums)+1)]
        count_hash={}
        
        for num in nums:
            try:
                count_hash[num]+=1
            except Exception as e:
                count_hash[num]=1
        
        for key in count_hash.keys():
            arr[count_hash[key]].append(key)
        len_arr=0
        final_arr=[]
        for i in range(len(nums),-1,-1):
            for j in arr[i]:
                final_arr.append(j)
                len_arr+=1
                if len_arr==k:
                    return final_arr
            
            if len_arr==k:
                return final_arr
            


