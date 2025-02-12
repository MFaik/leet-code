# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr_w_cnt = 0
        for i in range(k):
            if blocks[i] == 'W':
                curr_w_cnt += 1
        
        ret = curr_w_cnt
        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W':
                curr_w_cnt -= 1
            if blocks[i] == 'W':
                curr_w_cnt += 1
            ret = min(curr_w_cnt, ret)
        
        return ret
