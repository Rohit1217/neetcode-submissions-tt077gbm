class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        write_idx=0
        n=len(nums)

        for search_idx in range(1,n):
            if nums[search_idx]!=nums[search_idx-1]:
                nums[write_idx]=nums[search_idx-1]
                write_idx+=1

        nums[write_idx]=nums[n-1]
        write_idx+=1

        # print(n,n-1,write_idx)

        return write_idx 
        