class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=['+','-','*','/']
        i=0
        if len(tokens)==1:
            return int(tokens[0])

        stack.append(tokens[0])
        stack.append(tokens[1])
        i=2

        while i<len(tokens):
            new_token=tokens[i]
            if new_token in operators:
                operator=new_token
                a,b=int(stack.pop()),int(stack.pop())
                print(operator,i,a,b)
                if operator=="+":
                    result=a+b
                elif operator=="*":
                    result=a*b
                elif operator=="-":
                    result=b-a
                elif operator =="/":
                    result=b/a
                
                stack.append(result)
            else:
                stack.append(new_token)
            print(stack)
            i+=1

        return int(stack[0])
        