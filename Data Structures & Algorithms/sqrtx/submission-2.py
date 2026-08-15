class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        res=0
        right=x-1
        if x==1:
            return 1
        while left<=right:
            mid=(left+right)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                left=mid+1
                res=mid
            elif mid**2>x:
                right=mid-1
        
        return res