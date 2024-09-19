class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        i=0
        n=len(intervals)
        # Adding all the intervals before new intervals Starts
        while i<n and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i+=1

        # Merging all the intervals that overlap

        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(intervals[i][0],newInterval[0])
            newInterval[1]=max(intervals[i][1],newInterval[1])
            i+=1
        result.append(newInterval)
# Adding all the remaining intervals after the new interval
        while i<n:
            result.append(intervals[i])
            i+=1
        
        return result

# Time complexity O(n)