class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index=[]
        for i in range(len(nums)):
            flag=False
            j=i+1
            while j<len(nums):
                if(nums[i]+nums[j]==target):
                    index.append(i)
                    index.append(j)
                    return index
                j+=1
        return index
