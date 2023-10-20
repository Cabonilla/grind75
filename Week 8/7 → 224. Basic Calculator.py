class Solution:
    def calculate(self, s: str) -> int:
        ops = "+-*/"
        
        def update(op, n):
            if op == "+":
                stack.append(n)
            if op == "-":
                stack.append(-n)
            if op == "*":
                stack.append(stack.pop() * n)
            if op == "/":
                stack.append(int(stack.pop() / n))
                
        currNum, resNum = 0,0
        stack = []
        sign = "+"
        
        while currNum < len(s):
            if s[currNum].isdigit():
                resNum = resNum * 10 + int(s[currNum])
            elif s[currNum] in ops:
                update(sign, resNum)
                resNum = 0
                sign = s[currNum]
            elif s[currNum] == "(":
                resNum, j = self.calculate(s[currNum + 1:])
                currNum = currNum + j
            elif s[currNum] == ")":
                update(sign, resNum)
                return sum(stack), currNum + 1
            currNum += 1
        update(sign, resNum)
        return sum(stack)