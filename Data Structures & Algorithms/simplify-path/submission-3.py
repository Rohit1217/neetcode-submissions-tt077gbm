class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_stack=[]
        path_list=path.split("/")
        
        for dir_name in path_list:
            if dir_name!="" and dir_name!=".":
                if path_stack and dir_name=="..":
                    path_stack.pop()
                elif dir_name=="..":
                    continue
                else:
                    path_stack.append(dir_name)
        
        if path_stack==[]:
            return "/"

        simplified_path=""
        for path in path_stack:
            if path!="":
                simplified_path+="/"+path
        
        return simplified_path

