class Solution:
    def solution(self, a, b):
        answer = a + b
        return answer

if __name__ == "__main__":
    solution = Solution()
    a = input(" 첫번째 수 : ")
    b = input(" 두번째 수 : ")
    a = int(a)
    b = int(b)
    print(solution.solution(a, b))
