import random

# 1 ~ 45 의 list 생성
# range(n,m) = n부터 m-1 까지의 숫자를 생성
numbers = list(range(1, 46))

# numbers가 가진 숫자 중 무작위 값 6개 뽑기
print(random.sample(numbers, 6))

n=0
while n < 6:
    a=random.choice(numbers)
    numbers.remove(a)
    print(a)
    n = n+1

print(random.choices(numbers, k=6))
