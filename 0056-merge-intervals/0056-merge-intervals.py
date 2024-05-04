class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # if start[i+1] - start[i] < end[i+1] - end[i], they overlap
        intervals.sort(key= lambda interval : interval[0])
        if len(intervals) <= 1:
            return intervals
        new_intervals = [intervals[0]]
        s = 0
        e = 1
        for i in range(1,len(intervals),1):
            print(f"{intervals[i][s]}  {intervals[i-1][e]}")
            if intervals[i][s] <= new_intervals[-1][1]:
                new_intervals[-1][1] = max(intervals[i][e], new_intervals[-1][1])
            else:
                new_intervals.append(intervals[i])
        return new_intervals

    