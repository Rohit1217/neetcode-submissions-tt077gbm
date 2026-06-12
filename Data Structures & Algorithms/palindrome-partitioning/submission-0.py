class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        palindrome_part=[]
        curr_stack=[]
        
        def is_palindrome(s):
            i,j=0,len(s)-1
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def partition_rec(i):
            if i==len(s):
                palindrome_part.append(curr_stack.copy())

            for j in range(i+1,len(s)+1):
                if is_palindrome(s[i:j]):
                    curr_stack.append(s[i:j])
                    partition_rec(j)
                    curr_stack.pop()

            return

        
        partition_rec(0)
        
        return palindrome_part




