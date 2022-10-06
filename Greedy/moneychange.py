# 화폐교환

class Solution:
    def solution(self, money):

        title = " ### 화폐교환 ### "

        unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

        for i in unit:
            count = money // i
            money = money % i
            print(f'{i}원짜리 {count}개')

        '''

        a = money//unit[0]
        b = money%unit[0]//unit[1]
        c = money%unit[1]//unit[2]
        d = money%unit[2]//unit[3]
        e = money%unit[3]//unit[4]
        f = money%unit[4]//unit[5]
        g = money%unit[5]//unit[6]
        h = money%unit[6]//unit[7]

        '''
        
        return

if __name__ == '__main__':
    solution = Solution()
    money = input("교환 할 금액 입력 : ")
    print(solution.solution(int(money)))