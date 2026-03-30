class Solution:

    def encode(self, strs: List[str]) -> str:
        pos_code=""
        encoded_strs=""
        
        for word in strs:
            encoded_strs+=word
            pos_code+=str(len(word))+"_"
        
        encoded_strs+="|" + pos_code
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        res=[]
        pos_code=""
        idx=-1
        
        
        while s[idx]!="|":
            idx-=1
        
        
        while idx<-1:
            pos_code+=s[idx+1]
            idx+=1

        pos_code_list=pos_code.split("_")[:-1]

        start=0

        print(pos_code_list)
        for char in pos_code_list:
            res.append(s[start:int(char)+start])
            start=int(char)+start
        
        return res
