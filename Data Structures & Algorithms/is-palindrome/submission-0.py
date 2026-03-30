class Solution:
    def isPalindrome(self, s: str) -> bool:
        hash_map={}
        # s="Was it a car 99 or a cat I saw"
        # length=len(s)

        alpha_num="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        for char in alpha_num:
            hash_map[char]=True
        new_s=""
        for char in s:
            try:
                hash_map[char]
                new_s+=char.lower()
            except:
                continue
        
        i=0
        j=len(new_s)-1
        print(new_s)
        while j>i:
            if new_s[i]!=new_s[j]:
                print(new_s[i],new_s[j],i,j)
                return False
            else:
                i+=1
                j-=1
        return True
