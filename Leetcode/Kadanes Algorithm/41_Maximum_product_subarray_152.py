class Solution:
    def maxProduct(self, a):
        maxend=a[0]
        minend=a[0]
        result=a[0]

        for i in range(1,len(a)):
            v1=a[i]
            v2=maxend * a[i]
            v3=minend * a[i]
            maxend=max(v1,max(v2,v3))
            minend=min(v1,min(v2,v3))
            result=max(result,max(maxend,minend))
        return result