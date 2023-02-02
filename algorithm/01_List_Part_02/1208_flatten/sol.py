import sys
sys.stdin=open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    # 입력받은 dump값이 0이 아니라면 반복문을 계속 돌림
    while dump >= 0:
        # 박스의 최소값은 1이고 최댓값은 100 이므로 최대 최소의 조건 설정
        maxBox = 0
        maxIdx = 0
        minBox = 101
        minIdx = 0

        # 가로의 길이(배열의 길이) 는 항상 100으로 주어짐
        for i in range(100):
            if box[i] >= maxBox:        # dump가 1번 돌때 입력받은 box 리스트의 최댓값을 찾아줌
                maxBox = box[i]
                maxIdx = i              # index 값을 찾아온 box리스트의 최댓값에 해당하는 번호로 지정해줌

            # 위에서 최댓값을 찾은 후 최솟값을 찾으려면 elif 가 아닌 새로운 if문으로 들어가야 함
            if box[i] <= minBox:        #최솟값을 찾는 과정
                minBox = box[i]
                minIdx = i

        # 리스트를 순회하며 최댓값이 있는 box값을 1 줄이고
        # 최솟값이 있는 box값을 1 늘려줌
        box[maxIdx] -= 1
        box[minIdx] += 1

        # 종료 조건을 위해 dump값을 1씩 감소
        dump -= 1

        # 만약 dump 조건을 다 돌기전에 최대 - 최소가 1이나 0일 경우 반복문을 종료
        if maxBox - minBox == 0 or maxBox - minBox == 1:
            break
    print(f'#{tc} {maxBox - minBox}')

