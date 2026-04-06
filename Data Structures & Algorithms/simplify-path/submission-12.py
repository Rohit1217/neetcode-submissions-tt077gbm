class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_stack=[]
        path_list=path.split("/")
        
        for dir_name in path_list:
            if dir_name!="" and dir_name!=".":
                if path_stack and dir_name=="..":
                    path_stack.pop()
                elif dir_name!="..":
                     path_stack.append(dir_name)

        path_str="/"
        path_str+="/".join(path_stack)
                        
        return path_str

