class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/", "%"}

        for token in tokens:
            if token in operators:
                val = stack.pop()
                val2 = stack.pop()
                
                if token == "+":
                    stack.append(val2 + val)
                elif token == "-":
                    stack.append(val2 - val)
                elif token == "*":
                    stack.append(val2 * val)
                elif token == "/":
                    stack.append(int(val2 / val))
                elif token == "%":
                    stack.append(val2 % val)
            else:
                stack.append(int(token))

        return stack[-1]