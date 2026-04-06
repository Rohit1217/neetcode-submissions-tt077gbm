class Solution:
    def decodeString(self, s: str) -> str:
        
        bracket_stack=[]
        char_str="[abcdefghijklmnopqrstuvwxyz"

        for char in s:
            if char==']':
                sub_res=""
                
                while bracket_stack and bracket_stack[-1]!='[':
                    sub_res=bracket_stack.pop()+sub_res

                bracket_stack.pop()

                val_str=""
                while bracket_stack and bracket_stack[-1][0] not in char_str:
                    val_str=bracket_stack.pop()+val_str
                
                sub_res*=int(val_str)
                bracket_stack.append(sub_res)
            
            else:
                bracket_stack.append(char)
        
        res=("").join(bracket_stack)

        return res