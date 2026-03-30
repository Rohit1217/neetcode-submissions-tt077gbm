class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr1,arr2):
            
            res_arr=[]
            arr_1_idx=0
            arr_2_idx=0

            while arr_1_idx!=len(arr1) and arr_2_idx!=len(arr2):
                if arr1[arr_1_idx]<arr2[arr_2_idx]:
                    res_arr.append(arr1[arr_1_idx])
                    arr_1_idx+=1
                else:
                    res_arr.append(arr2[arr_2_idx])
                    arr_2_idx+=1

            if len(arr1)!=arr_1_idx:
                res_arr=res_arr +arr1[arr_1_idx:]        
            elif len(arr2)!=arr_2_idx:
                res_arr=res_arr +arr2[arr_2_idx:]
                
            return res_arr   
        
        def sort_rec(nums):
            if len(nums)==1:
                return nums
            else:
                mid=len(nums)//2
                return merge(sort_rec(nums[:mid]),sort_rec(nums[mid:]))

        return sort_rec(nums)            