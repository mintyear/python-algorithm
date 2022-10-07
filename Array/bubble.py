# 랜덤숫자

import random

class Solution:
    def solution(self):
        keys = ['first','second','rhird','forth','fifth']
        dc = {}

        print('### 랜덤숫자 ###')
        print("*"*30)
        
        for i in keys:
            dc[i] = random.randint(1,100)

        for k,v in dc.items():
            print(f'{k} : {v}')

        print("*"*30)

if __name__ == '__main__':
    solution = Solution()
    solution.solution()
