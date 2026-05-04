class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==0:
            return -1
        
        succ_next=1
        if s[-1]=="0":
            succ=0
        else:
            succ=1

        if len(s)==1:
            return succ
        for idx in range(len(s)-2,-1,-1):
            temp=succ
            if int(s[idx:idx+2])<27 and s[idx]!="0":
                succ=succ+succ_next
            elif s[idx]=="0":
                succ=0
            succ_next=temp
        
        return succ
            
            

