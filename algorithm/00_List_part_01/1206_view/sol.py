import sys
sys.stdin=open('input.txt')

# 테스트 케이스 10만큼 반복
for tc in range(1, 11):
    N = int(input())
    bd = list(map(int, input().split()))

    # 건물 길이만큼 배열 만들기
    arr = [0] * N

    # 건물의 양끝은 0 이므로 비교 안함
    for i in range(2, N-2):
        # 건물의 높이 차이를 저장해둘 리스트 생성
        difference = []
        for j in range(i-2, i+3):
            # 조사할 기준건물은 bd[i]의 조망권
            # bd[i] 가 옆건물 보다 크다는건 조망권이 확보 되었다는 뜻
            if i == j:
                continue
            # 자기 자신을 제외한 옆건물의 높이가 자신보다 작다면 그 차이만큼 조망권이 확보 되었다는 의미
            # 이중에서 제일 작은 값을 가져와야 하기에 차이를 저장해둘 리스트를 만들어야 함
            # 기준건물에서 옆건물의 높이를 뺏을때 양수값이면 그 값을 difference에 넣어주고
            # 음수일때 difference에 0을 넣어줌
            if bd[i] - bd[j] > 0:
                difference.append((bd[i]-bd[j]))
            else:
                difference.append(0)

        # 반복문을 다 돌았을 때 가장 작은 값을 가져와야 하기에 반복문을 다시 돌려줌
        minV = difference[0]
        for k in difference:
            if minV > k:
                minV = k

        # 반복문을 다 돌았으므로 건물별로 조망권을 가지는 세대 수를 arr 에넣어줌
        arr[i] = minV

    # 양수값을 가지는 arr의 수를 구해야 함
    cnt_bd = 0
    for i in arr:
        cnt_bd += i

    print(f'#{tc} {cnt_bd}')