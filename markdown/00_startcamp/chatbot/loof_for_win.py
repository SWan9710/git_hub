import random

while True:
    number = list(range(1, 3))
    CH_num = random.choice(number)
    user_str = input('가위, 바위, 보 중 입력해주세요.\n')
    user_num = 0

    if user_str == '가위':
        user_num = 1
        if CH_num == 1:
            print('무승부')
        elif CH_num == 2:
            print('졌습니다.')
        elif CH_num == 3:
            print('이겼습니다.')
            break
    elif user_str == '바위':
        user_num = 2
        if CH_num == 2:
            print('무승부')
        elif CH_num == 3:
            print('졌습니다.')
        elif CH_num == 1:
            print('이겼습니다.')
            break
    elif user_str == '보':
        user_num = 3
        if CH_num == 3:
            print('무승부')
        elif CH_num == 1:
            print('졌습니다.')
        elif CH_num == 2:
            print('이겼습니다.')
            break
    else:
        print('잘못된 입력입니다.')



