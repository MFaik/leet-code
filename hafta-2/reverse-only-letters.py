# https://leetcode.com/problems/reverse-only-letters/
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = list(s)
        while True:
            while l < r and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isalpha():
                r -= 1
            if l >= r:
                break
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
