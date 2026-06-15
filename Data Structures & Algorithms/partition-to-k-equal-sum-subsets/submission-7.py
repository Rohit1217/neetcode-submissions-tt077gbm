class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        res=False
        nums.sort(reverse=True)
        
        bucket_sums=[0 for _ in range(k)]
        target=sum(nums)//k

        if sum(nums)%k!=0 or nums[0]>target:
            return False

        def part_k_subset_rec(i):
            nonlocal res

            if res:
                return

            elif i==len(nums):
                res=True
                return
            
            for j in range(k):
                if bucket_sums[j]+nums[i]>target:
                    continue
                
                bucket_sums[j]+=nums[i]
                part_k_subset_rec(i+1)
                bucket_sums[j]-=nums[i]

                if bucket_sums[j]==0:
                    break
            
            return

        part_k_subset_rec(0)
        return res