class Solution:
    def solution(self, money):

        title = " ### 화폐교환 ### "
        astar = "*"*30
        values = f'요청금액 : {money} 원\n'

        return f'{astar}\n{title}\n{values}\n{astar}'

if __name__ == '__main__':
    solution = Solution()
    money = input("교환 할 금액 입력 : ")
    print(solution.solution(money))