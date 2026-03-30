from collections import deque
import numpy as np

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q=deque()
        q2=deque()
        visited=set()
        rows,cols=len(heights),len(heights[0])
        
        pacific=[]
        atlantic=[]
        for i in range(rows):
            pacific.append([])
            atlantic.append([])
            for j in range(cols):
                pacific[i].append(0)
                atlantic[i].append(0)
                if i==0 or j==0: 
                    q.append((i,j))
                    pacific[i][j]=1
                if i==rows-1 or j==cols-1:
                    q2.append((i,j))
                    atlantic[i][j]=1

        
        while len(q)>0:
            i,j=q.popleft()
            neighbors=[(i+1,j),(i,j+1),(i,j-1),(i-1,j)]
            for i_new,j_new in neighbors:
                if i_new>rows-1 or j_new>cols-1 or i_new<0 or j_new<0 or pacific[i_new][j_new]!=0:
                    continue
                elif heights[i_new][j_new]>=heights[i][j]:
                    q.append((i_new,j_new))
                    pacific[i_new][j_new]=1
        
        while len(q2)>0:
            i,j=q2.popleft()
            neighbors=[(i+1,j),(i,j+1),(i,j-1),(i-1,j)]
            for i_new,j_new in neighbors:
                if i_new>rows-1 or j_new>cols-1 or i_new<0 or j_new<0 or atlantic[i_new][j_new]!=0:
                    continue
                elif heights[i_new][j_new]>=heights[i][j]:
                    q2.append((i_new,j_new))
                    atlantic[i_new][j_new]=1
        result=[]
        print(pacific,atlantic)
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j]+atlantic[i][j]==2:
                    result.append([i,j])
            
        return result
        