from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadends=set(deadends)
        queue=deque([("0000",0)])
        visited=set()

        def get_neighbors(pattern):
            neighbors=[]
            for i in range(len(pattern)):
                curr_num=int(pattern[i])
                prev,nxt=str((curr_num-1)%10),str((curr_num+1)%10)
                
                for j in (prev,nxt):
                    prefix_pattern=pattern[:i]
                    
                    if i<len(pattern)-1:
                        suffix_pattern=pattern[i+1:]
                    else:
                        suffix_pattern=""

                    neighbors.append(prefix_pattern + j + suffix_pattern)
            
            return neighbors
        
        while queue:
            pat,d=queue.popleft()

            if pat in deadends or pat in visited:
                continue
            
            if pat==target:
                return d

            visited.add(pat)
            neighbors=get_neighbors(pat)

            for neighbor in neighbors:
                n_pat,n_d=neighbor,d+1
                queue.append((n_pat,n_d))

        
        return -1
        
        





