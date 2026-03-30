class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        freq_hash_s1,freq_hash_window={},{}
        
        for char in s1:
            freq_hash_s1[char]=freq_hash_s1.get(char,0)+1
            freq_hash_window[char]=freq_hash_window.get(char,0)

        left_idx=0
        right_idx=len(s1)-1


        for idx in range(right_idx):
            freq_hash_window[s2[idx]]=freq_hash_window.get(s2[idx],0)+1
       
        while right_idx<len(s2):            
            flag=True
            freq_hash_window[s2[right_idx]]=freq_hash_window.get(s2[right_idx],0)+1

            print(freq_hash_window)
            for char in freq_hash_s1:
                if freq_hash_s1[char]!=freq_hash_window[char]:
                    flag=False
            
            if flag==True:
                return True

            left_idx+=1
            right_idx+=1
            freq_hash_window[s2[left_idx-1]]=freq_hash_window.get(s2[left_idx-1])-1
            
        
        return False
