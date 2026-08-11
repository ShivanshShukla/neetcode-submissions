class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums = []
        for i in range(len(nums)):
            if nums[i] != val:
                new_nums.append(nums[i])
        for i in range(len(new_nums)):
            nums[i]=new_nums[i]
        return len(new_nums)
