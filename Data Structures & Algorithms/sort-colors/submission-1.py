class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer =0             
        for i in range(len(nums)):
            if nums[i]==0:
                nums[pointer],nums[i]=nums[i],nums[pointer]
                pointer+=1
        for i in range(len(nums)):
            if nums[i]==1:
                nums[pointer],nums[i]=nums[i],nums[pointer]
                pointer+=1


        