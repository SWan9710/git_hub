import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)

# 원소 N개의 모든 경우의 수
# 2**N -> 1 << N 과 같다.
# 원소의 개수가 3개라고 할때
# 2**3 == 8
# 1<<3 -> 2진수(1000) 이기 때문에 이는 10진수로 바꾸면 -> 8
# 0001 -> 1을 왼쪽으로 3번 밀면
# 1000 이다.
    for i in range(1, 1<<N):  # N = len(arr) -> 10개의 정수이므로 10
        result = 0         # 2^10의 모든 경우의 수 판별 1부터 2^N번째의 경우의 수
        for j in range(N): # 모든 요소의 개수
            if i & (1<<j):
                result += arr[j]
        if result == 0:
            print(1)
            break
    else:
        print(0)