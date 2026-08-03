class Node:
    def __init__(self,end=False):
        self.children={}
        self.end=end

class PrefixTree:
    def __init__(self):
        self.root=Node()
        
    def insert(self, word: str) -> None:
        root=self.root
        n=len(word)
        for i in range(n):
            char=word[i]
            if char in root.children:
                root=root.children[char]
            else:
                for j in range(i,n):
                    char=word[j]
                    root.children[char]=Node()
                    root=root.children[char]
                root.end=True
                return                

        root.end=True
        return 

    def search(self, word: str) -> bool:
        root=self.root
        n=len(word)

        for i in range(n):
            char=word[i]
            if char in root.children:
                root=root.children[char]
            else:
                return False
        
        if root.end==True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        root=self.root
        n=len(prefix)

        for i in range(n):
            char=prefix[i]
            if char in root.children:
                root=root.children[char]
            else:
                return False
        return True
        