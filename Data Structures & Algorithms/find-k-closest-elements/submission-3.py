class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_idx=0
        min_val=1e16
        n=len(arr)

        for idx in range(n):
            if abs(x-arr[idx])<min_val:
                min_idx=idx
                min_val=abs(x-arr[idx])

        left,right=min_idx-1,min_idx+1
        curr_len=right-left-1
        
        while curr_len!=k:    
            if left<0:
                right=right+(k-curr_len)
            
            elif right>n-1:
                left=left-(k-curr_len)

            elif abs(x-arr[left])<=abs(x-arr[right]):
                left-=1
            else:
                right+=1
            curr_len=right-left-1
        
        return arr[left+1:right]


