class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        name=defaultdict(str)
        parent=defaultdict(str)
        rank=defaultdict(int)

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]


        def union(x,y):
            rootx,rooty=find(x),find(y)

            if rootx==rooty:
                return

            if rank[rootx]>rank[rooty]:
                parent[rooty]=rootx
            elif rank[rootx]<rank[rooty]:
                parent[rootx]=rooty
            else:
                parent[rooty]=rootx
                rank[rootx]+=1
            
            return
        

        for account in accounts:
            ac_name,primary_mail=account[0],account[1]

            if primary_mail not in parent:
                parent[primary_mail]=primary_mail
                rank[primary_mail]=1
                name[primary_mail]=ac_name

            for mail in account[1:]:
                if mail not in parent:
                    parent[mail]=mail
                    rank[mail]=1
                    name[mail]=ac_name

                union(primary_mail,mail)
        
        for mail in parent:
            find(mail) 

        conn_comp=defaultdict(list)

        for mail in parent:
            conn_comp[parent[mail]].append(mail)
        
        res=[]
        for primary_mail in conn_comp:
            sub_res=[name[primary_mail]]
            sub_res=sub_res+sorted(conn_comp[primary_mail])
            res.append(sub_res)

        return res

                 
