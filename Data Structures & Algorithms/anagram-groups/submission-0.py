def checkAnagram(string1,string2):
    char_hash={}
    if len(string1)!=len(string2):
        return False

    for char in string1:
        try:
            char_hash[char]+=1
        except Exception as e:
            char_hash[char]=1

    for char in string2:
        try:
            char_hash[char]-=1
        except Exception as e:
            return False
    
    for char in char_hash.keys():
        if char_hash[char]!=0:
            return False
    return True      


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list=[]
        anagram_hash={}
        for i in range(len(strs)):
            flag=False
            for j in range(i):
                if checkAnagram(strs[i],strs[j]):
                    flag=True
                    anagram_hash[strs[j]].append(strs[i])
                    break
            if not flag:
                anagram_hash[strs[i]]=[strs[i]]
        for anagram in anagram_hash.keys():
            anagram_list.append(anagram_hash[anagram])
        return anagram_list
