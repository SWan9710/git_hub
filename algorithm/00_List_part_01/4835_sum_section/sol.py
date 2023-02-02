import sys
sys.stdin=open('input.txt')

test_case = int(input())
for tc in range(1,test_case+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    arr = [0] * (N-M+1)
    for i in range(N-M+1): # 0 ~ 8까지 i에 들어감
        result = 0
        for j in range(i, i+M): # 0일때 0,1,2 가 j에 할당
            result += ai[j]
        arr[i] = result
    maxV = arr[0]
    minV = arr[0]

    for j in range(len(arr)):
        if maxV < arr[j]:
            maxV = arr[j]
        if minV > arr[j]:
            minV = arr[j]

    print(f'#{tc} {maxV - minV}')