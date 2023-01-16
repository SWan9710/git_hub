import requests
import random

#확인할 회차받기
# num = input()
num = 1049

# 로또 url 가져오기
url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'

# 입력받은 회차의 당첨번호 확인하기 -> 6개
result = requests.get(url).json()

# 로또 당첨번호 1 ~ 6까지 출력
# win_num 이라는 빈 리스트 0 ~ 5에 각각 result 해서 얻어온 로또 번호를 리스트에 추가해줌 append 함수 써서
win_num = []
for i in range(1, 7):
    win_num.append(result[f'drwtNo{i}'])
print(win_num)

count_list = {
    '1등' : 0,
    '2등' : 0,
    '3등' : 0,
    '4등' : 0,
    '5등' : 0,
    '꽝' : 0,
}

for roll in range(100000):
    pick_num = random.sample(range(1, 46), 6)
    # pick_num에 랜덤번호 1 ~ 6을 생성해서 넣는걸 roll만큼 반복

    count = 0
    for my_pick_num in pick_num:    #pick_num[0] 부터 [5]까지의 수가 한번씩 my_pick_num에 들어감
        if my_pick_num in win_num:  #my_pick_num 가 가지는 값은 pick_num[0]에 해당하는 값 이 값이 win_num의 리스트에 있으면 count 에 + 1을 하라는 의미
            count = count + 1
    if count == 6:
        count_list['1등'] = count_list['1등'] + 1
        print('----------1----------')
    elif count == 5 and result['bnusNo'] in pick_num:
        count_list['2등'] = count_list['2등'] + 1
        print('-----2-----')
    elif count == 5:
        count_list['3등'] = count_list['3등'] + 1
        print('--3--')
    elif count == 4:
        count_list['4등'] = count_list['4등'] + 1
        print('4')
    elif count == 3:
        count_list['5등'] = count_list['5등'] + 1
        print('5')
    elif count <= 2:
        count_list['꽝'] = count_list['꽝'] + 1
        print('.')

print(count_list)
    