class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==0:
            return 0
        
        stack=[int(tokens[0])]
        next_idx=1

        while next_idx!=len(tokens):
            next_val=tokens[next_idx]
            
            if next_val=="+":
                a,b=stack.pop(),stack.pop()
                stack.append(a+b)
            elif next_val=="-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)            
            elif next_val=="*":
                a,b=stack.pop(),stack.pop()
                stack.append(a*b)
            elif next_val=="/":
                a,b=stack.pop(),stack.pop()
                if b//a<0 and b//a!=b/a:
                    stack.append(b//a+1)
                else:
                    stack.append(b//a)

            else:
                stack.append(int(next_val))

            next_idx+=1

        return stack[0]