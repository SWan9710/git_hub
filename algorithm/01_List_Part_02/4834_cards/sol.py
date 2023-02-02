import sys
sys.stdin=open('input.txt')

test_case = int(input())
for tc in range(1,test_case+1):
    # 카드 장수 최소 5 최대 100
    card_n = int(input())
    deck = [0] * 10
    card_ai = int(input())

    # 카드배열 만들기
    for i in range(card_n):
        deck[card_ai%10] += 1
        card_ai //= 10

    max_card = 0
    idx_card_num = deck[0]

    for i in range(len(deck)):

        # 제일 많은 카드 수 구하기
        if deck[i] >= max_card:
            max_card = deck[i]
            idx_card_num = i

    print(f'#{tc} {idx_card_num} {max_card}')






