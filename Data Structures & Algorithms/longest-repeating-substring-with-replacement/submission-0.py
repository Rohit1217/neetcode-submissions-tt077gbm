class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_hash={}
        max_len=0
        max_occur=0
        curr_max_char=''
        successor=''
        i=0
        for j in range(len(s)):
            char=s[j]
            if char in count_hash and j>=i:
                count_hash[s[j]]+=1
            else:
                count_hash[s[j]]=1
            
            if count_hash[s[j]]>max_occur:
                max_occur=count_hash[s[j]]
                curr_max_char=s[j]
                successor=""

            elif count_hash[s[j]]==max_occur:
                successor=s[j]

            if j-i+1-max_occur>k:
                print(i,s[i],count_hash[s[i]])
                count_hash[s[i]]-=1
                if curr_max_char==s[i]:
                    if successor=="":
                        max_occur=-1
                    else:
                        curr_max_char=successor
                        successor=""
                i+=1
            else:
                max_len+=1
        return max_len

