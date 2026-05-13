class Solution:
    def decodeString(self, s: str) -> str:
        
        stack=[]
        digit="0123456789"
        curr_digit=0
        decoded_str=""

        for char in s:
            if char in digit:
                curr_digit=curr_digit*10+int(char)
            
            elif char=="[":
                stack.append(curr_digit)
                stack.append(char)
                curr_digit=0
            
            elif char=="]":
                curr_substr=""
                curr_elem=stack.pop()
                
                while curr_elem!="[":
                    curr_substr=curr_elem+curr_substr
                    curr_elem=stack.pop()

                curr_substr=stack.pop()*curr_substr
                stack.append(curr_substr)

            else:
                stack.append(char)
        
        return ("").join(stack)