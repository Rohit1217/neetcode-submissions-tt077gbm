class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)

        wordset=set(wordDict)
        
        #wordbreak[i]= max(wordbreak(j) for word in   wordDict where j-i=len(word))
        
        if n==0:
            return

        succ_cut=[n+1]*(n+1)
        wordbreak=[False]*(n+1)
        wordbreak[n]=True


        for i in range(n,-1,-1):
            if wordbreak[i]:
                continue

            for word in wordDict:
                len_w=len(word)
                if s[i:i+len_w] in wordset and i+len_w<n+1:
                    wordbreak[i]=wordbreak[i] or wordbreak[i+len_w]

                    if wordbreak[i]==True:
                        succ_cut[i]=len_w
                        break
        
        print(succ_cut)
        return wordbreak[0]




