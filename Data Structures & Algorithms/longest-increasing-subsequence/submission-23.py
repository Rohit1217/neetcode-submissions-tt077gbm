import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pat=[]


        for num in nums:
            idx=bisect.bisect_left(pat,num)

            if idx==len(pat):
                pat.append(num)
            else:
                pat[idx]=num
        
        return len(pat)