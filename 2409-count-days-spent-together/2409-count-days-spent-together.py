class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if arriveAlice > leaveBob or arriveBob > leaveAlice:
            return 0

        arrive = max(arriveAlice, arriveBob)
        leave = min(leaveAlice, leaveBob)
        arrive_month = int(arrive[0:2])
        arrive_day = int(arrive[3:])
        leave_month = int(leave[0:2])
        leave_day = int(leave[3:])
        ret = 0

        print(arrive_month, arrive_day, leave_month, leave_day)
        if arrive_month + 1 <= leave_month:
            for month in range(arrive_month, leave_month):
                ret += days[month - 1]
        ret += leave_day - arrive_day        

        return ret + 1