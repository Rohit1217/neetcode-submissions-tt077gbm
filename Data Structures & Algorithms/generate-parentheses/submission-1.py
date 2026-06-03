from collections import defaultdict

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenth_arr=[]
        curr_parenth=[]

    
        counts=defaultdict(int)

        def parenthize_rec():
            if len(curr_parenth)==2*n:
                parenth_arr.append(("").join(curr_parenth))
                return
            
            if counts["("]>counts[")"] and counts[")"]<n:
                curr_parenth.append(")")
                counts[")"]+=1

                parenthize_rec()
                
                curr_parenth.pop()
                counts[")"]-=1

            
            if counts["("]<n:
                curr_parenth.append("(")
                counts["("]+=1

                parenthize_rec()
                
                curr_parenth.pop()
                counts["("]-=1

           
            return
        
        parenthize_rec()
        return parenth_arr
    



