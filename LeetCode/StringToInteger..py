### https://leetcode.com/problems/reverse-integer/
## Thuan - 23.11.14

import re

class Solution(object):
    def myAtoi(self, s):
        if len(s) == 0:
            return 0
        num = [int(i) for i in re.findall(r'-?\d+\.?\d*', s)]
        if num[0] > pow(2, 31) - 1:
            return pow(2,31) - 1
        if num[0] < (-1)*pow(2, 31):
            return (-1)*pow(2,31)
        return num[0]



if __name__ == '__main__':
    solu = Solution()
    print(solu.myAtoi("words and 987"))