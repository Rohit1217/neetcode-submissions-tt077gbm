class Solution:
    def __init__(self):
        self.res_list=[]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        def subset_rec(i,sub_res):
            for j in range(2):
                if j!=0:
                    sub_sub_res=sub_res+[nums[i]]
                else:
                    sub_sub_res=sub_res+[]
                    
                if i==len(nums)-1:
                    self.res_list.append(sub_sub_res)
                else:
                    subset_rec(i+1,sub_sub_res)
            
        sub_res=[]
        subset_rec(0,[])
        return self.res_list
        

