class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median_array=[]
        l1=len(nums1)
        l2=len(nums2)
        i,j=0,0
        while i<l1 and j<l2:
            if nums1[i]<=nums2[j]:
                median_array.append(nums1[i])
                i+=1
            elif nums2[j]<=nums1[i]:
                median_array.append(nums2[j])
                j+=1
        while j<l2:
            median_array.append(nums2[j])
            j+=1
        while i<l1:
            median_array.append(nums1[i])
            i+=1

        if len(median_array)%2==0:
            mid=len(median_array)//2
            return(float(median_array[mid-1]+median_array[mid])/2)
        else:
            mid=len(median_array)//2
            return(float(median_array[mid]))
