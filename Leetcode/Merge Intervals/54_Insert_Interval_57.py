class Solution:
    from typing import List
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res1 = []
        insert=False
        for i in range(len(intervals)):
            start = intervals[i][0]

            if insert == False and start >= newInterval[0]:
                res1.append(newInterval)
                insert = True

            res1.append(intervals[i])
        if insert == False:
            res1.append(newInterval)

        res = []
        start1 = res1[0][0]
        end1 = res1[0][1]

        for i in range(1, len(res1)):
            start2 = res1[i][0]
            end2 = res1[i][1]

            if end1 >= start2:
                end1 = max(end1, end2)
                #res.append([start1, end1])
            else:
                res.append([start1, end1])
                start1 = start2
                end1 = end2

        # for loop khatam
        res.append([start1, end1])
        return res