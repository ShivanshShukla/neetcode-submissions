class Solution:
    def isValid(self, s: str) -> bool:
        open_stack=[]
        open_bracket={"(","{","["}
        close_bracket={")","}","]"}
        for bracket in s:
            if bracket in open_bracket:
                open_stack.append(bracket)
            else:
                if (len(open_stack)==0):
                    return False
                if "()"==open_stack[-1]+bracket:
                    open_stack.pop()
                elif "[]"==open_stack[-1]+bracket:
                    open_stack.pop()
                elif "{}"==open_stack[-1]+bracket:
                    open_stack.pop()
                else:
                    return False
        return True if len(open_stack)==0 else False
