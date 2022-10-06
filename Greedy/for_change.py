# 반복문(금액 입력)

class Solution:
    def solution(self,money):

        a = [50000,10000,5000,1000,500,100,50,10]

        for i in a:
            count = money // i
            money = money % i
            print(f'{i}원 짜리 {count}개')
        return

if __name__ == '__main__':
    solution = Solution()
    money = input("교환 할 금액 입력 : ")
    print(solution.solution(int(money)))