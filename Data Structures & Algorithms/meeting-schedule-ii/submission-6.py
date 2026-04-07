"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        events = []
        for meeting in intervals:
            events.append((meeting.start, 1))
            events.append((meeting.end, -1))
        
        occupancy = 0
        events.sort()
        for time, delta in events:
            occupancy += delta
            res = max(res, occupancy)
        return res


            
            
