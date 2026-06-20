from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        prev_count,prev_char=0,""
        res=""

        used_char=0

        char_heap=[]
        char_count=Counter(s)

        for char,count in char_count.items():
            char_heap.append((-count,char))

        heapq.heapify(char_heap)

        while char_heap:
            count,curr_char=heapq.heappop(char_heap)

            if prev_count!=0:
                heapq.heappush(char_heap,(prev_count,prev_char))
            
            prev_count,prev_char=count+1,curr_char
            used_char+=1
            res+=prev_char
        
        if used_char!=len(s):
            return ""
        else:
            return res

