class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo=[-1 for i in range(len(s))]
        self.n=len(s)

        def numDecodings_memo(i):
            if i ==self.n-1 and int(s[i])==0:
                self.memo[i]=0
                return 0
            elif i==self.n-1:
                self.memo[i]=1
                return 1
            if i>self.n-2:
                return 1
            if self.memo[i]!=-1:
                return self.memo[i]
            if int(s[i])==0:
                self.memo[i]=0
            elif int(s[i])>2:
                self.memo[i]=numDecodings_memo(i+1)
            elif int(s[i+1])==0:
                self.memo[i]=numDecodings_memo(i+2)
            elif int(s[i])==2 and int(s[i+1])>6:
                self.memo[i]=numDecodings_memo(i+1)
            elif int(s[i])==2 and int(s[i+1])<=6 and int(s[i])!=0:
                self.memo[i]=numDecodings_memo(i+1)+numDecodings_memo(i+2)
            else:
                self.memo[i]=numDecodings_memo(i+1)+numDecodings_memo(i+2)
            return self.memo[i]
        numDecodings_memo(0)
        print(self.memo)
        return self.memo[0]

        