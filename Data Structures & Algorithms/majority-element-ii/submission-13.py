class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<3:
            return nums
        else:
            history_buffer=[[min(nums),1],[max(nums),1]]
        res_set=set()

        for idx in range(0,len(nums)):
            curr_num=nums[idx]

            if history_buffer[0][0]==curr_num:
                history_buffer[0][1]+=1

            elif history_buffer[1][0]==curr_num:
                history_buffer[1][1]+=1
            
            elif history_buffer[0][1]==1:
                history_buffer[0]=[curr_num,1]        
            
            else:
                history_buffer[0][1]-=1
            
            if history_buffer[0][1]>history_buffer[1][1]:
                history_buffer[1],history_buffer[0]=history_buffer[0],history_buffer[1]

        guess_arr=[hist[0] for hist in history_buffer]

        for guess in guess_arr: 
            count=0  
            for num in nums:
                if num==guess:
                    count+=1
            if count>len(nums)//3:
                res_set.add(guess)
        
        print(history_buffer)
        res=list(res_set)
        return res
