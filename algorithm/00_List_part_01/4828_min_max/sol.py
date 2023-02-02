import sys
sys.stdin=open('input.txt')

test_case = int(input()) # 첫째줄에 입력받는 test_case의 수

for tc in range(1, test_case+1): # 순서출력을 위해 1부터 test_case의 +1 까지 반복
    N = int(input()) # 둘째줄에 입력받는 리스트의 길이
    ai = list(map(int, input().split())) # 공백으로 입력받은 리스트를 쪼개기
    maxV = 0 # 최고값을 저장할 임시변수
    for i in ai:
        if i > maxV:
            maxV = i # 반복문의 최종 결과값을 저장

    minV = ai[0] # ai의 첫번째 값을 minV에 할당
    for j in ai:
        if minV > j:
            minV = j # 반복문의 최종 결과값을 저장
    result = maxV - minV
    print(f'#{tc} {result}')


