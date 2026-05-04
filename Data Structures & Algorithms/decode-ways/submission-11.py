class Solution:
    def numDecodings(self, s: str) -> int:
        
        n=len(s)
        memo=[-1]*n

        def numDecoding_rec(i):
            if i==n-1 and s[i]=="0":
                return 0
            elif i==n or i==n-1:
                return 1
            elif memo[i]!=-1:
                return memo[i]
            else:
                if int(s[i:i+2])<27 and s[i]!="0":
                    memo[i]=numDecoding_rec(i+1)+numDecoding_rec(i+2)
                elif int(s[i])==0:
                    memo[i]=0
                else:
                    memo[i]=numDecoding_rec(i+1)
            return memo[i]
        
        numDecoding_rec(0)
        print(memo)
        return numDecoding_rec(0)
