# https://leetcode.com/problems/basic-calculator-ii/
class Solution:
    def calculate(self, s: str) -> int:
        ret = 0
        mul_pass = 1
        curr = 0
        op = '*'
        for c in s:
            if c.isnumeric():
                curr *= 10
                curr += int(c)
            elif c.isspace():
                continue
            else:
                if op == '*':
                    mul_pass *= curr
                else:
                    mul_pass = int(mul_pass/curr)
                curr = 0
                match(c):
                    case "+":
                        ret += mul_pass
                        mul_pass = 1
                        op = '*'
                    case "-":
                        ret += mul_pass
                        mul_pass = -1
                        op = '*'
                    case "/":
                        op = '/'
                    case "*":
                        op = '*'
        if op == '*':
            mul_pass *= curr
        else:
            mul_pass = int(mul_pass/curr)
        ret += mul_pass
        return ret
