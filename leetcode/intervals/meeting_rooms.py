from typing import List, Tuple


class Solution:
    def canAttendMeetings(self, intervals: List[Tuple[int, int]]) -> bool:
        if len(intervals) == 1:
            return True

        # Sort the intervals by their start times
        intervals = sorted(intervals, key=lambda x: x[0])

        for i in range(1, len(intervals)):
            cur_start, _ = intervals[i]
            prev_start, prev_end = intervals[i - 1]

            if prev_start <= cur_start and prev_end >= cur_start:
                return False

        return True


sol = Solution()
print(sol.canAttendMeetings([(0, 30), (5, 10), (15, 20)]))
print(sol.canAttendMeetings([(5, 8), (9, 15)]))
