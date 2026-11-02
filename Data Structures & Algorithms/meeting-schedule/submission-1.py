class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)

        res = []
        res.append(intervals[0])

        for item in range(1, len(intervals)):
            top = res[-1]

            if top.end > intervals[item].start:
                return False

            res.append(intervals[item])

        return True