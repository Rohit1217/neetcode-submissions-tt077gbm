class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo=[None for i in range(len(s))]

        def wordbreak_rec(i):
            if i==len(s):
                return True
            
            elif i>len(s):
                return False
            
            elif memo[i] is not None:
                return memo[i]
            
            else:
                ans=False
                for word in wordDict:
                    len_word=len(word)

                    if len_word+i>len(s):
                        continue
                    
                    elif s[i:i+len_word]==word:
                        curr_ans=wordbreak_rec(i+len_word)

                        if curr_ans==True:
                            memo[i]=True
                            return memo[i]
                
                memo[i]=False
                return memo[i]
        
        ans=wordbreak_rec(0)
        print(memo)
        return ans
