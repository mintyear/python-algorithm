"""
90 이상은 A 학점
80 이상은 B 학점
70 이상은 C 학점
60 이상은 D 학점
50 이상은 E 학점
그 이하는 F 학점
"""

class Solution:
    def solution(self, a, b, c):
        title = " ### 성적표 ### "
        total = a + b + c
        avg = round(total/3,1)
        if avg >= 90:
            grade = "A학점"
        elif avg >= 80:
            grade = "B학점"
        elif avg >= 70:
            grade = "C학점"
        elif avg >= 60:
            grade = "D학점"
        elif avg >= 50:
            grade = "E학점"
        else:
            grade = "F학점"
        return f"{title} \n 총점 : {total}, 평균 : {avg}, 학점 : {grade}"

if __name__ == "__main__":
    solution = Solution()
    a = int(input(" 국어 성적 : "))
    b = int(input(" 영어 성적 : "))
    c = int(input(" 수학 성적 : "))
    print(solution.solution(a,b,c))