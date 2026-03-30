class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash={}

        alpha="abcdefghijklmnopqrstuvwxyz"
        alpha_idx={}
        
        for i in range(len(alpha)):
            alpha_idx[alpha[i]]=i
        
        for string in strs:
            l=[0 for i in range(len(alpha))]
            
            for char in string:
                idx=alpha_idx[char]
                l[idx]+=1
            
            enc_str=""
            for idx in range(len(l)):
                enc_str+=str(l[idx])+"|"
            
            if enc_str not in anagram_hash.keys():
                anagram_hash[enc_str]=[string]
            else:
                anagram_hash[enc_str].append(string)

        print(anagram_hash)
        anagram_list=[]
        for key in anagram_hash.keys():
            anagram_list.append(anagram_hash[key])
        return anagram_list

        


