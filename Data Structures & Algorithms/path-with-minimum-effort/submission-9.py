import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        start=(0,0)
        rows,cols=len(heights),len(heights[0])
        heap=[(0,start)]

        heapq.heapify(heap)
        visited=set()

        while heap:
            d,curr_node=heapq.heappop(heap)
            row,col=curr_node

            if curr_node in visited:
                continue
            visited.add(curr_node)
            # print(curr_node,d)
            if curr_node==(rows-1,cols-1):
                return d
            
            neighbors=[(row-1,col),(row+1,col),(row,col-1),(row,col+1)]

            for neighbor in neighbors:
                nr,nc=neighbor

                if neighbor not in visited and nr>=0 and nc>=0 and nr<rows and nc<cols :
                    nd=abs(heights[row][col]-heights[nr][nc])
                    heapq.heappush(heap,(max(nd,d),neighbor))

                    

        return -1        