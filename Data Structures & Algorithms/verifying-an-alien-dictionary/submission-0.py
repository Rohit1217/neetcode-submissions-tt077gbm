class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        og_order="abcdefghijklmnopqrstuvwxyz"
        order_map={}
        
        for i in range(len(order)):
            order_map[order[i]]=og_order[i]

        if len(words)==1:
            return True


        prev_word=""
        for char in words[0]:
            prev_word+=order_map[char]

        for i in range(1,len(words)):
            curr_word=""
            for char in words[i]:
                curr_word+=order_map[char]

            if curr_word<prev_word:
                return False
            
            prev_word=curr_word

        return True
