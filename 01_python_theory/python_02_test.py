# 조건표현식(삼항연산자)

num = 5
result = '홀수' if num % 2 else '짝수'
print(result)

num = -5
value = num if num >= 0 else 0
print(value)

grades = {'john':80,'eric':90}
for student in grades:
    print(student)

grades = {'john':80,'eric':90}
for student in grades:
    print(student, grades[student])

grades = {'john':80,'eric':90}
for student in grades:
    print(grades.keys())

grades = {'john':80,'eric':90}
for student in grades:
    print(grades.values())

grades = {'john':80,'eric':90}
for student in grades:
    print(grades.items())