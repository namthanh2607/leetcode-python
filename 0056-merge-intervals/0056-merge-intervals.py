class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        if len(intervals) == 1:
            return intervals
        ret = [intervals[0]]
        start = 0
        end = 1
        while end < len(intervals):
            if ret[start][1] >= intervals[end][0] and ret[start][1] <= intervals[end][1]:
                ret[start][1] = intervals[end][1]
                end += 1
            elif ret[start][1] >= intervals[end][0] and ret[start][1] > intervals[end][1]:
                end += 1
            else:
                ret.append(intervals[end])
                start += 1
                end += 1
        return ret
            

        