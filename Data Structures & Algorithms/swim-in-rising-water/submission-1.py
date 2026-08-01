import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        nr,nc=len(grid),len(grid[0])

        heap=[(grid[0][0],(0,0))]
        heapq.heapify(heap)

        visited=set((0,0))
        time=0

        while heap:
            d,cell=heapq.heappop(heap)
            r,c=cell

            if cell in visited:
                continue

            if cell==(nr-1,nc-1):
                time+=max(0,d-time)
                return time

            # print(cell,time,d)
            visited.add(cell)
            time+=max(0,d-time)
            neighbors=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]

            for neighbor in neighbors:
                ner,nec=neighbor    
                if neighbor not in visited and ner>-1 and nec>-1 and ner<nr and nec<nc:
                    d=grid[ner][nec]
                    heapq.heappush(heap,(d,(ner,nec)))
        
        return time





