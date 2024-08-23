class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows,Cols=len(heights),len(heights[0])
        Pac,atl=set(),set()
        res=[]

        def dfs(r,c,visit,PrevHeight):
            if ( (r,c) in visit or
                r<0 or
                r==Rows or
                c<0 or
                c==Cols or
                heights[r][c]<PrevHeight):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(Cols):
            dfs(0,c,Pac,heights[0][c])
            dfs(Rows-1,c,atl,heights[Rows-1][c])
        for r in range(Rows):
            dfs(r,0,Pac,heights[r][0])
            dfs(r,Cols-1,atl,heights[r][Cols-1])

        for r in range(Rows):
            for c in range(Cols):
                if (r,c) in Pac and (r,c) in atl:
                    res.append((r,c))
        return res
