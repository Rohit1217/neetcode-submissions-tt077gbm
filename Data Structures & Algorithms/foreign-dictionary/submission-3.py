class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #TIme to do dfs topological sort

        adj_list={}

        def make_graph(words):
            for i in range(1,len(words)):
                curr,nexxt=words[i-1],words[i]
                
                cmp_range=min(len(curr),len(nexxt))

                flag=True
                for i in range(cmp_range):
                    if curr[i] not in adj_list:
                        adj_list[curr[i]]=[]

                    if curr[i]==nexxt[i]:
                        continue
                    else:
                        adj_list[curr[i]].append(nexxt[i])
                        flag=False
                        break
                
                if flag:
                    if len(curr)>len(nexxt):
                        return False

                for j in range(i,len(curr)):
                    if curr[j] not in adj_list:
                        adj_list[curr[j]]=[]
            
            curr=words[len(words)-1]
            for i in range(0,len(curr)):
                if curr[i] not in adj_list:
                    adj_list[curr[i]]=[]            

        flag=make_graph(words)

        if flag==False:
            return ""
        
        visited=set()
        processing=set()
        is_cycle=False

        top_list=[]

        def dfs(u):
            nonlocal is_cycle
            if is_cycle:
                return
            
            processing.add(u)
            
            if u in adj_list:
                for v in adj_list[u]:
                    if v in processing:
                        is_cycle=True
                        return
                    
                    elif v not in visited:
                        dfs(v)

            processing.remove(u)
            visited.add(u)
            top_list.append(u)

            return
        print(adj_list)
        for u in adj_list:
            if u not in visited:
                dfs(u)
            
            if is_cycle:
                return ""

        print(top_list)
        top_list.reverse()
        return ("").join(top_list)



        

