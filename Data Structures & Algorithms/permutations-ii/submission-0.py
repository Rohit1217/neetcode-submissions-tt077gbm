from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        counter=Counter(nums)
        
        permutations=[]
        curr_permutation=[]

        def gen_permutations_rec():
            if len(curr_permutation)==len(nums):
                permutations.append(curr_permutation.copy())
                return
            
            for unique_num in counter:
                if counter[unique_num]!=0:
                    curr_permutation.append(unique_num)
                    counter[unique_num]-=1
                    
                    gen_permutations_rec()

                    curr_permutation.pop()
                    counter[unique_num]+=1
            return

        gen_permutations_rec()
        return permutations                   

