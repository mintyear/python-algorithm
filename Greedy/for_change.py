# 반복문(딕셔너리, 리스트 사용)

class Solution:
    def solution(self, money):

        a = [50000,10000,5000,1000,500,100,50,10] # 자료구조, 대수(상수)
        dc = {}

        print('### 화폐교환 ###')
        print("*"*30)
        print(f'요청금액 : {money} 원')

        for i in a: # 알고리즘, 리스트
            cnt = money // i
            dc[i] = cnt
            money = money % i

        for k,v in dc.items(): # 딕셔너리 # k, v 자동으로 앞의 값이 key가 됨
            print(f'{k}원 : {v} 매')
        print("*"*30)

if __name__ == '__main__':
    solution = Solution()
    money = input('교환을 원하는 금액 입력 : ')
    solution.solution(int(money))