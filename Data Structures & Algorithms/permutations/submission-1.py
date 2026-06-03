class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        curr_permutation=[]
        visited=set()


        def permute_rec():
            if len(curr_permutation)==len(nums):
                permutations.append(curr_permutation.copy())
                return
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    curr_permutation.append(num)
                    
                    permute_rec()
                    
                    visited.discard(num)
                    curr_permutation.pop()

        permute_rec()
        return permutations
