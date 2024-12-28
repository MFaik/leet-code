# https://leetcode.com/problems/crawler-log-folder/
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for dir in logs:
            if dir == "./":
                continue
            if dir == "../":
                if cnt > 0:
                    cnt -= 1
                continue
            cnt += 1
        return max(cnt, 0)
