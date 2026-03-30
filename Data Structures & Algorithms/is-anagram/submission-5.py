class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if s=="" and t=="":
        #     return True
        # elif s=="" or t=="":
        #     return False
        if len(s) != len(t):
            return False
        char_map_s={}
        
        for char in s:
            if char in char_map_s:
                char_map_s[char]+=1
            else:
                char_map_s[char]=1

        for char in t:
            if char not in char_map_s:
                return False
            else:
                char_map_s[char]-=1
        
        for char in char_map_s.keys():
            if char_map_s[char]!=0:
                return False
        
        return True