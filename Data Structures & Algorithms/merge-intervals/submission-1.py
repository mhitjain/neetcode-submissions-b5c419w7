class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return 
        intervals.sort()
        res = [intervals[0]]
        for i in range(len(intervals)-1):
            cur = res[-1]
            nxt = intervals[i+1]
            if nxt[0]<=cur[1]:
                if nxt[1]>=cur[1]:
                    res[-1][1]=nxt[1]
            else:
                res.append(nxt)
        return res

