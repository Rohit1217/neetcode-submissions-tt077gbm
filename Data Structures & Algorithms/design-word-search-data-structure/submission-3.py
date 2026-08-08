from collections import deque
class Node:
    def __init__(self):
        self.children={}
        self.end=False


class WordDictionary:
    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        curr=self.root
        n=len(word)
        for i in range(n):
            char=word[i]
            if char in curr.children:
                curr=curr.children[char]
            
            else:
                for j in range(i,n):
                    char=word[j]
                    curr.children[char]=Node()
                    curr=curr.children[char]
                
                curr.end=True
                return

        curr.end=True
        return

    def search(self, word: str) -> bool:
        curr=self.root
        i=0
        flag=False

        def dfs(curr,i):
            nonlocal flag

            if flag or (i>=len(word)):
                return 

            char=word[i]
            
            if char!=".":
                if (char in curr.children):
                    if i==len(word)-1: 
                        flag=curr.children[char].end
                    else:
                        dfs(curr.children[char],i+1)
                else:
                    return 
            
            if char==".":
                if i==len(word)-1:
                    for child in curr.children:
                        if curr.children[child].end:
                            flag=True
                else:
                    for child in curr.children:
                        dfs(curr.children[child],i+1)
            
            return
        
        dfs(curr,0)
        return flag
