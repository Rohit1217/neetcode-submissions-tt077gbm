import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        n=len(nums)

        def decompose(n,k):
            result = []
            remaining = k

            while remaining >= 2:
                k = remaining
                # Find largest k coprime with n
                while math.gcd(n, k) != 1:
                    k -= 1
                result.append(k)
                remaining -= k

            if remaining > 0:
                result.append(remaining)  # append leftover 1 if any

            return result

        k_list=decompose(n,k)
        for k in k_list:
            temp=nums[(0)%n]
            for idx in range(n):
                val=nums[((idx+1)*k)%n]
                nums[((idx+1)*k)%n]=temp
                temp=val


        return