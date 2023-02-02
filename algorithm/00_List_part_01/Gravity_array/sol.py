import sys
sys.stdin=open('input.txt')
test_case = int(input()) # 테스트케이스

for tc in range(1, test_case+1):
    N = int(input()) # 방의 크기
    box = list(map(int, input().split()))
    result = 0
    for i in range(N):
        count = 0
        for j in range(i, N):
            if box[i] > box[j]:
                count += 1
        if result < count:
            result = count
    print(f'#{tc} {result}')


