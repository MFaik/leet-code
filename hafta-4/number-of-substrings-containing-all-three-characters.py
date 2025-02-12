# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def get_index(c: str) -> int:
            return ord(c)-ord('a')

        n = len(s)
        cnt = [0, 0, 0]
        r = 0
        while r < n and prod(cnt) == 0:
            cnt[get_index(s[r])] += 1
            r += 1
        
        if prod(cnt) == 0:
            return 0
        
        ret = n-r+1
        for l in range(n):
            cnt[get_index(s[l])] -= 1
            while r < n and prod(cnt) == 0:
                cnt[get_index(s[r])] += 1
                r += 1
            
            if prod(cnt) != 0:
                ret += n-r+1
        return ret
