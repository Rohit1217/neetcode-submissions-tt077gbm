def get_freq_hash(string):
    hash={}
    alpha_str='abcdefghijklmnopqrstuvwxyz'
    s=""
    for char in alpha_str:
        hash[char]=0
    for char in string:
        hash[char]+=1
    for char in alpha_str:
        s+=f'{char}{hash[char]}'
    return s


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list=[]
        anagram_hash={}
        for i in range(len(strs)):
            s=get_freq_hash(strs[i])
            try:
                anagram_hash[s].append(strs[i])
            except Exception as e:
                anagram_hash[s]=[strs[i]]
        for anagram in anagram_hash.keys():
            anagram_list.append(anagram_hash[anagram])
        return anagram_list
