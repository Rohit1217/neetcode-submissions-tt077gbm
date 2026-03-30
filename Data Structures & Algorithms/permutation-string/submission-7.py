class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_hash={}
        match_hash={}
        num_matches=0
        i=0

        if len(s2)<len(s1):
            return False

        for char in s1:
            if char  in freq_hash:
                freq_hash[char]+=1
            else:
                freq_hash[char]=1

        req_matches=len(freq_hash.keys())

        for char in freq_hash.keys():
            match_hash[char]=0


        for j in range(len(s1)):
            if  s2[j] in freq_hash:
                match_hash[s2[j]]+=1

        for char in match_hash.keys():
            if freq_hash[char]==match_hash[char]:
                num_matches+=1

        if num_matches==req_matches:
            return True
        else:
            i+=1
            j+=1
        while j<len(s2):
            char1=s2[i-1]
            char2=s2[j]
            
            if char1 in freq_hash:
                if freq_hash[char1]==match_hash[char1]:
                    num_matches-=1
                match_hash[char1]-=1
                if freq_hash[char1]==match_hash[char1]:
                    num_matches+=1
            
            if char2 in freq_hash:
                if freq_hash[char2]==match_hash[char2]:
                    num_matches-=1
                match_hash[char2]+=1
                if freq_hash[char2]==match_hash[char2]:
                    num_matches+=1


            if num_matches==req_matches:
                return True
            i+=1
            j+=1    

        
        return False




        