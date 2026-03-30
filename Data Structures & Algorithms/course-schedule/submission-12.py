class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list={}
        discovery_time={}
        finish_time={}
        visited=set()
        timer=0

        for dep in (prerequisites):
            source,target=dep[0],dep[1]
            if source in adj_list.keys():
                adj_list[source].append(target)
            else:
                adj_list[source]=[target]
        
        print(adj_list)

        def dfs(node,timer,flag):
            timer+=1
            discovery_time[node]=timer
            # print(adj_list,node,finish_time,discovery_time)
            if node in adj_list.keys():
                for new_node in adj_list[node]:
                    print(new_node,finish_time.keys(),visited,flag,adj_list)
                    if new_node not in visited:
                        visited.add(new_node)
                        timer,flag=dfs(new_node,timer,flag)
                    elif new_node not in finish_time.keys():
                        return timer,False

            timer+=1
            finish_time[node]=timer
            return timer,flag
        flag=True
        for node in adj_list.keys():
            if node not in visited:
                visited.add(node)
                timer,flag=dfs(node,timer,flag)
                print(flag)
                if flag==False:
                    return False
        
        return True
        