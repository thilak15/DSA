class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        i=0
        s=0
        while i<len(boxTypes) and truckSize>0:
            if truckSize>=boxTypes[i][0]:
                s+=(boxTypes[i][0]*boxTypes[i][1])
                truckSize-=boxTypes[i][0]
            else:
                s+=(truckSize)*(boxTypes[i][1])
                truckSize=0
            i+=1
        return s
    # Time Complexity O(n)
    # Space Complexity O(1)