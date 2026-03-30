class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def get_unique_key(char_count_hash):
            s=""
            for char in char_count_hash:
                s+=str(char_count_hash[char])+"|"
            return s

        def initialize_hash():
            hash={}
            s="abcdefghijklmnopqrstuvwxyz"
            for char in s:
                hash[char]=0
            return hash

        res_hash={}
        res_list=[]

        for word in strs:
            char_hash=initialize_hash()
            for char in word:
                char_hash[char]+=1
            
            key=get_unique_key(char_hash)

            if key in res_hash:
                res_hash[key].append(word)
            else:
                res_hash[key]=[word]
        
        for unique_key in res_hash:
            res_list.append(res_hash[unique_key])
        
        return res_list