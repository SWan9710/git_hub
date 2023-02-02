import sys
sys.stdin=open('input.txt')

test_case = int(input())

for tc in range(test_case):
    # 카드는 0 ~ 9까지
    card_num = int(input())

    #run 검사를 위해 더미카드 index 10과 11을 생성
    card_list = [0] * 12
    # 6장의 카드로만 이루어짐
    for i in range(6):
        # 해당하는 카드 넘버에 갯수 +1
        card_list[card_num % 10] += 1
        card_num = card_num // 10

    i = 0
    triplet = 0
    run = 0
    while i < 10:
        if card_list[i] >= 3:
            triplet +=1
            card_list[i] -= 3
            continue

        if card_list[i] and card_list[i+1] and card_list[i+2] >= 1:
            card_list[i] -= 1
            card_list[i+1] -= 1
            card_list[i+2] -= 1
            run += 1
            continue
        i += 1

    if triplet + run == 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')