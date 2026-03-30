class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """    
        n=len(s)
        start_idx,end_idx=0,n-1

        while start_idx<end_idx:
            temp=s[start_idx]
            s[start_idx]=s[end_idx]
            s[end_idx]=temp

            start_idx+=1
            end_idx-=1
        