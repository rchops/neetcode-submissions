class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # add numbers to stack
        # if top of stack is operator do current op and add back to stack
        stack = []
        for i in range(len(tokens)):
            # add to stack if number
            if tokens[i] == "+":
                first = stack.pop()
                second = stack.pop()
                res = first + second
                stack.append(res)
            elif tokens[i] == "-":
                first = stack.pop()
                second = stack.pop()
                res = second - first
                stack.append(res)
            elif tokens[i] == "*":
                first = stack.pop()
                second = stack.pop()
                res = first * second
                stack.append(res)
            elif tokens[i] == "/":
                first = stack.pop()
                second = stack.pop()
                res = second / first
                stack.append(int(res))
            else:
                stack.append(int(tokens[i]))

        return int(stack[0])