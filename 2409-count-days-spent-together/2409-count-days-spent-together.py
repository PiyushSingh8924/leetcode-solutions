class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        if start > end:
            return 0
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def conv(date):
            mon = int(date[:2])
            day = int(date[3:])
            return sum(days[:mon - 1]) + day
        return conv(end) - conv(start) + 1

