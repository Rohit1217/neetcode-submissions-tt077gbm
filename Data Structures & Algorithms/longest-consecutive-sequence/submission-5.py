class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_hash={}
        child_hash={}

        for num in nums:
            len_hash[num]=-1
        
        for num in nums:
            if (num+1) in len_hash:
                child_hash[num]=1
            else:
                child_hash[num]=-1
        
        def assign_len(num):
            if len_hash[num]!=-1:
                return len_hash[num]
            elif child_hash[num]==-1:
                len_hash[num]=1
                return len_hash[num]
            else:
                len_hash[num]=1+assign_len(num+1)
                return  len_hash[num]
        
        for num in nums:
            assign_len(num)
        
        maxm=0
        for num in len_hash:
            maxm=max(maxm,len_hash[num])
        return maxm