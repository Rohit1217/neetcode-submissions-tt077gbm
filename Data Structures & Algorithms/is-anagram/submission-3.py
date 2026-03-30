class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_hash={}
        for char in s:
            try:
                char_hash[char]+=1
            except Exception as e:
                char_hash[char]=1
        for char in t:
            try:
                char_hash[char]=char_hash[char]-1
            except Exception as e:
                return False
        for char in char_hash.keys():
            # print(char_hash[char],char)
            if char_hash[char]!=0:
                return False
        return True