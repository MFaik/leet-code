# https://leetcode.com/problems/keyboard-row/
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1, r2, r3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        ret = []
        for word in words:
            single_row = True
            is_r1, is_r2, is_r3 = False, False, False
            for c in word.lower():
                is_r1 |= c in r1
                is_r2 |= c in r2
                is_r3 |= c in r3
                if(is_r1 + is_r2 + is_r3 > 1):
                    single_row = False
                    break
            if single_row:
                ret.append(word)
        return ret
