class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for item in nums:
            m[item] = m.get(item, 0) + 1
        max_key = max(m, key=m.get)   
        return max_key