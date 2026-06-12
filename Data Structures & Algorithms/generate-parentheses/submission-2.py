class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        parenth_arr=[]
        left,right=0,0
        parenth_stack=[]

        def generate_parenth_rec(left,right):
            if left==n and right==n:
                parenth_arr.append(("").join(parenth_stack))
                return

            if left>right and right<n:
                parenth_stack.append(")")
                right+=1
                generate_parenth_rec(left,right)
                parenth_stack.pop()
                right-=1
            
            if left<n:
                parenth_stack.append("(")
                left+=1
                generate_parenth_rec(left,right)
                parenth_stack.pop()
                left-=1
                return
    
        generate_parenth_rec(0,0)
        return parenth_arr
