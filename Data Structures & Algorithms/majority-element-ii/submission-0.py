class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority=len(nums)/3
        counts_dict = {}
        val=[]
        for num in nums:
            counts_dict[num] = counts_dict.get(num, 0) + 1

        for num, freq in counts_dict.items():
            if freq>majority:
                val.append(num)
        return val