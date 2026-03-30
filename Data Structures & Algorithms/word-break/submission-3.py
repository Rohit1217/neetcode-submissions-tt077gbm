class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo=[-1 for _ in range(len(s))]
        n=len(s)
        t=max([len(s) for s in wordDict])

        def wordBreak_memo(i):
            if i>n-1:
                return True
            elif self.memo[i]!=-1:
                return self.memo[i]
            else:
                for word in wordDict:
                    j=i+len(word)
                    print(word,s[i:j])
                    if s[i:j]==word:
                        ans=wordBreak_memo(j)
                        if ans==True:
                            self.memo[i]=True
                            return self.memo[i]
                self.memo[i]=False
                return self.memo[i]
        wordBreak_memo(0)
        return self.memo[0]
             
        