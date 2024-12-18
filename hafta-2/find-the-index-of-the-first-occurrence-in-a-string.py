# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        dp = [0]
        curr = 0
        n = 1
        while n < len(needle):
            print(n, curr)
            if needle[n] == needle[curr]:
                curr += 1
            elif curr != 0:
                curr = dp[curr-1]
                continue
            dp.append(curr)
            n += 1
        
        target = len(needle)
        n = 0
        h = 0
        while h < len(haystack):
            if haystack[h] == needle[n]:
                n += 1
                if n == target:
                    return h-target+1
            elif n != 0:
                n = dp[n-1]
                continue
            h += 1
        return -1
