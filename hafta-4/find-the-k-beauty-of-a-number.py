# https://leetcode.com/problems/find-the-k-beauty-of-a-number/
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        ret = 0
        for i in range(k, len(s)+1):
            curr = int(s[i-k:i])
            if curr != 0 and num % curr == 0:
                ret += 1
        return ret
