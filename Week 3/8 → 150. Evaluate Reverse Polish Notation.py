class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens:
            if t not in '+-*/':
                stk.append(int(t))
            else:
                nm = stk.pop()
                if t == "+":
                    stk[-1] += nm
                elif t == "-":
                    stk[-1] -= nm
                elif t == "*":
                    stk[-1] *= nm
                else:
                    stk[-1] = int(stk[-1]/nm)

        return stk[0]