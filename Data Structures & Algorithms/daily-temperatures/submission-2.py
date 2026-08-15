class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        result=[0]*len(temperatures)
        for i,temps in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temps:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result