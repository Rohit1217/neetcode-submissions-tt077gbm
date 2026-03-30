class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result={}


        for i  in range(len(temperatures)):
            result[i]=0

        for i in range(len(temperatures)-1,-1,-1):
            j=i+1
            while j<len(temperatures) and j!=0:
                print(j,temperatures[j],i)
                if temperatures[j]>temperatures[i]:
                    result[i]=j
                    j=len(temperatures)+1
                else:
                    j=result[j]
        print(result)
        res_arr=[]
        for i in range(len(temperatures)):
            if result[i]!=0:
                res_arr.append(result[i]-i)
            else:
                res_arr.append(0)
        return res_arr
            

        