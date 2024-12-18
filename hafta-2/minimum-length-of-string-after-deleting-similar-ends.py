# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                break
            curr = s[l]
            while l <= r and s[l] == curr:
                l += 1
            while l <= r and s[r] == curr:
                r -= 1
        return r-l+1
