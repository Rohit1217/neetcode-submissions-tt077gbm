class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pause=False
        i=0
        j=0
        min_len=len(s)+1
        sstring=""
        num_matches=0
        i_opt,j_opt=None,None

        freq_hash={}
        match_hash={}

        for char in t:
            if char in freq_hash:
                freq_hash[char]+=1
            else:
                freq_hash[char]=1

        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            match_hash[char]=0
            if char not in freq_hash:
                num_matches+=1

        while j<len(s):
            if pause==False:
                if s[i] not in freq_hash:
                    i+=1
                if s[j] in freq_hash:
                    match_hash[s[j]]+=1
                    if  match_hash[s[j]]==freq_hash[s[j]]:
                        num_matches+=1
                
                if num_matches==52:
                    pause=True
                    if j-i+1<min_len and num_matches==52:
                        min_len=j-i+1
                        i_opt,j_opt=i,j 
                else:
                    j+=1

            else:
                # print(match_hash["A"],match_hash["B"],match_hash["C"])
                if s[i] not in freq_hash:
                    i+=1
                elif freq_hash[s[i]]==match_hash[s[i]]:
                    if j-i+1<min_len and num_matches==52:
                        min_len=j-i+1
                        i_opt,j_opt=i,j

                    num_matches-=1
                    pause=False
                    match_hash[s[i]]-=1
                    i+=1
                    j+=1                    
                else:
                    match_hash[s[i]]-=1
                    i+=1  
            # print(pause,i,j,min_len,num_matches)
        if i_opt is not None and j_opt is not None:
            sstring=s[i_opt:j_opt+1]
        return sstring

                

        