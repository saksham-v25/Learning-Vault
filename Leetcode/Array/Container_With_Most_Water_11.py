class Solution:
    from typing import List
    def maxArea(self, height: List[int]) -> int:
        res=0
        l=0
        r=len(height)-1
        while l < r:
            width=r - l
            length=min(height[l],height[r])
            area=length * width
            res=max(res,area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return res
        
        