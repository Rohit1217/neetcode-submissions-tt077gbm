class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        # After the loop, low and high are the two closest candidates
        if low >= n: 
            min_idx = n - 1
        elif high < 0: 
            min_idx = 0
        else:
            min_idx = low if abs(x - arr[low]) < abs(x - arr[high]) else high

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


