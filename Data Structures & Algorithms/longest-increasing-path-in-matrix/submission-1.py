class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m,n=len(matrix),len(matrix[0])
        dp=[[None for i in range(n)] for j in range(m)]
        

        def path_rec(i,j):
            if dp[i][j] is not None:
                return dp[i][j]
            else:
                max_path=0
                neighbors=((i-1,j),(i+1,j),(i,j-1),(i,j+1))

                for neighbor in neighbors:
                    nr,nc=neighbor

                    if nr==m or nc==n or nr<0 or nc<0:
                        continue

                    if matrix[nr][nc]>matrix[i][j]:
                        max_path=max(max_path,1+path_rec(nr,nc))
                dp[i][j]=max_path
                return max_path
        
        max_val=0
        for r in range(m):
            for c in range(n):
                max_val=max(max_val,path_rec(r,c))
        
        return max_val+1
        
