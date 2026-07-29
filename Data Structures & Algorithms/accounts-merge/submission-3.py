class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        

        parent={}
        name_hash={}
        rank=defaultdict(int)

        def find(x):
            if parent[x]==x:
                return x
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
            name=account[0]
            name_hash[account[1]]=name

            for j in range(1,len(account)):
                if account[j] in parent:
                    union(parent[account[j]],account[1])
                else:
                    parent[account[j]]=account[1]
                    union(account[j],account[1])
                    

        
        res_hash=defaultdict(list)
        res=[]

        for mail in parent:
            rep_mail=find(mail)
            res_hash[rep_mail].append(mail)

        for mail in res_hash:
            mail_list=res_hash[mail]
            mail_list.sort()
            res.append([name_hash[mail]]+mail_list)

        return res 

            