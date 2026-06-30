class Solution:
    from typing import List
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1) #for i
        n=len(nums2) #for j
        res=[]
        i=0
        j=0
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            
            else:#nums2[j] < nums1[i]
                res.append(nums2[j])
                j+=1 

        
        while j<n:
            res.append(nums2[j])
            j+=1
            
        
        while i<m:
            res.append(nums1[i])
            i+=1
        l=len(res)
        if l % 2 == 0:
            left = res[l//2 -1]
            right = res[l//2]
            return (left + right) / 2
        else:
            return res[l // 2]
