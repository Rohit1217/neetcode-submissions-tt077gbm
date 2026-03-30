class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        flag=False
        
        if nums==[]:
            return 0

        def swap_block(start,end,block_size,num_arr):
            for idx in range(start+block_size,end):
                num_arr[idx-block_size]=num_arr[idx]


        def swap(nums,i,val_pos_list):
            curr_block_size=i+1
            curr_pos=val_pos_list[i]

            if curr_block_size==len(val_pos_list):
                if curr_pos!=len(nums)-1:
                    swap_block(curr_pos-curr_block_size+1,len(nums),curr_block_size,nums)
                return i+1,True

            else:
                next_pos=val_pos_list[i+1]
                swap_block(curr_pos-curr_block_size+1,next_pos,curr_block_size,nums)
                return i+1,False
        

        val_pos_list=[]

        for idx in range(len(nums)):
            if nums[idx]==val:
                val_pos_list.append(idx)
        
        if val_pos_list==[]:
            return len(nums)
        
        idx=0

        while not flag:
            idx,flag=swap(nums,idx,val_pos_list)
            print(nums)

        return len(nums)-len(val_pos_list)

