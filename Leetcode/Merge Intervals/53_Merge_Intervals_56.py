class Solution:
    from typing import List
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        start1=intervals [0][0]
        end1 = intervals [0][1]
        
        for i in range (1,len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if end1 >= start2: #overlap hoo rha hai isliye merge karoo

                end1 = max(end1, end2)
                continue
            res.append([start1, end1])

            start1 = start2
            end1 = end2
        # for loop end here
        res.append([start1, end1])

        return res   

        
