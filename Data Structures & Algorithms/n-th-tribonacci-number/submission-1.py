class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1

        first,second,third=0,1,1

        for i in range(n-2):
            # print(n-2,third)

            fourth=first+second+third

            first,second,third=second,third,fourth
        
        return third