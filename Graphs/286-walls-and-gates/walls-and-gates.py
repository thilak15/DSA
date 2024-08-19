class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        Rows,Cols=len(rooms),len(rooms[0])
        Visit=set()
        q=deque()
        def addrooms(r,c):
            if(min(r,c)<0 or r==Rows or c==Cols or (r,c) in Visit or rooms[r][c]==-1):
                return
            Visit.add((r,c))
            q.append([r,c])

        for r in range(Rows):
            for c in range(Cols):
                if rooms[r][c]==0:
                    q.append([r,c])
                    Visit.add((r,c))
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                rooms[r][c]=dist
                addrooms(r+1,c)
                addrooms(r-1,c)
                addrooms(r,c+1)
                addrooms(r,c-1)
            dist+=1
        