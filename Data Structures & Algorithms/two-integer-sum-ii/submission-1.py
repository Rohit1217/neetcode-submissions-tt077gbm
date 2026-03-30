class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while(i<j):
            diff=target-(numbers[j]+numbers[i])
            if diff==0:
                return [i+1,j+1]
            elif diff<0:
                j=j-1
            else:
                i=i+1
