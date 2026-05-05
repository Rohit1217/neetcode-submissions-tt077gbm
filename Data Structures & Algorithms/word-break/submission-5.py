class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set=set(wordDict)
        word_len=set([len(word) for word in wordDict])
        n=len(s)
        
        memo=[-1]*n

        def word_break_rec(i):
            if i>n:
                return 0
            elif i==n:
                return 1
            elif memo[i]!=-1:
                return memo[i]
            else:
                ans=0
                for size in word_len:
                    if s[i:i+size] in word_set:
                        ans=max(ans,word_break_rec(i+size))
                memo[i]=ans
            
            return memo[i]
        
        ans=word_break_rec(0)
        
        if ans==1:
            return True
        return False
        


        