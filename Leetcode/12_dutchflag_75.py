class Solution:
    def sortColors(self, arr):
        start=0
        mid=0
        end=len(arr)-1

        while mid<=end :

            if arr[mid]==0:
                temp=arr[mid]
                arr[mid]=arr[start]
                arr[start]=temp
                start+=1
                mid+=1


            elif arr[mid]==1:
                mid+=1


            else: # arr[mid]==2
                temp=arr[mid]
                arr[mid]=arr[end]
                arr[end]=temp
                end-=1
        return arr