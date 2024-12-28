# https://leetcode.com/problems/remove-outermost-parentheses/
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ret = []
        cnt = 0
        for c in s:
            if c == ")":
                cnt -= 1
            if cnt != 0:
                ret.append(c)
            if c == "(":
                cnt += 1
        return "".join(ret)
