class Solution:
    def maxAbsoluteSum(self, a):
        def max_sum(a):
            i=0
            best_ending=a[i]
            ans_max=a[i]
            for i in range(1,len(a)):
                v1=best_ending+a[i]
                v2=a[i]
                best_ending=max(v1,v2)
                ans_max=max(ans_max,best_ending)
            return ans_max

        def min_sum(a):
            i=0
            best_ending=a[i]
            ans_min=a[i]
            for i in range(1,len(a)):
                v1=best_ending+a[i]
                v2=a[i]
                best_ending=min(v1,v2)
                ans_min=min(ans_min,best_ending)
            return ans_min
           
       
        abs_max=max_sum(a)
        abs_min=min_sum(a)
        maximum_abs_sum=max(abs(abs_max),abs(abs_min))
    
        return maximum_abs_sum
      

        