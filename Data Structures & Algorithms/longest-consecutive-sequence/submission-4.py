
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        maxm=0
        hash_table={}
        for i in range(len(nums)):
            hash_table[nums[i]]=1
        for i in range(len(nums)):
            try:
                 if hash_table[nums[i]-1]:
                    continue
            except:
                count=1
                j=nums[i]
                while True:
                    try:
                        hash_table[j+1]
                        count+=1
                        j+=1
                    except:
                        break
            if count>maxm:
                maxm=count
        return maxm