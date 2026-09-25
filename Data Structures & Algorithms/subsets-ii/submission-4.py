class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res=[]
        curr=[]

        n=len(nums)

        def sub_rec(i):
            if i==n:
                res.append(curr.copy())
                return
            else:
                j=i+1
                while j<n and nums[i]==nums[j]:
                    j+=1
                
                sub_rec(j)
                
                curr.append(nums[i])
                sub_rec(i+1)
                curr.pop()
        
        sub_rec(0)
        return res