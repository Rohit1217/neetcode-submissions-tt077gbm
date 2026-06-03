class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets=[]
        curr_subset=[]
        n=len(nums)

    
        def subset_rec(i):
            if i==n:
                subsets.append(curr_subset.copy())
                return

            j=n
            for k in range(i+1,n):
                if nums[k]!=nums[i]:
                    j=k
                    break

            subset_rec(j)

            curr_subset.append(nums[i])
            subset_rec(i+1)
            curr_subset.pop()
        
        
        subset_rec(0)

        return subsets