class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res_arr=[]

        arr1_ptr=0
        arr2_ptr=0
        
        while (arr1_ptr+arr2_ptr)<(n+m):
            if arr1_ptr<m and arr2_ptr<n:
                
                if nums1[arr1_ptr]<nums2[arr2_ptr]:
                    res_arr.append(nums1[arr1_ptr])
                    arr1_ptr+=1
                else:
                    res_arr.append(nums2[arr2_ptr])
                    arr2_ptr+=1
            
            elif arr1_ptr==m:
                print(res_arr,"asdsad",arr2_ptr)
                res_arr+=nums2[arr2_ptr:n]
                arr2_ptr=n
            
            else:
                print(res_arr,"asasd")
                res_arr+=nums1[arr1_ptr:m]
                arr1_ptr=m
        
        print(res_arr)
        for idx in range(len(res_arr)):
            nums1[idx]=res_arr[idx]

        return 