"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # 1. Separate and sort start and end times
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])

        s_ptr, e_ptr = 0, 0
        count, res = 0, 0

        # 2. Iterate through all start times
        while s_ptr < len(intervals):
            # If a meeting starts before the earliest ending meeting finishes
            if start_times[s_ptr] < end_times[e_ptr]:
                count += 1
                s_ptr += 1
            else:
                # A meeting finished, freeing up a room
                count -= 1
                e_ptr += 1
            
            res = max(res, count)
            
        return res


            
            
