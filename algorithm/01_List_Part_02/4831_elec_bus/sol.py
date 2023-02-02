import sys
sys.stdin=open('input.txt')

# 첫 줄에 노선 수 T가 주어진다 (1 <= T <= 50)
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. 1이상 ~ 100이하의 수
# N 정류장의 수 = 배열의 길이
# K 최대 이동 거리
# M 충전기가 설치된 정류장의 번호

test_case = int(input())
for tc in range(1, test_case+1):
    K, N, M = map(int, input().split())

    charge_station = list(map(int,input().split()))

    # 정류장의 전체 길이에 해당하는 리스트에 골인지점까지 해서 +1 해줌
    station_arr = [0] * (N+1)

    # 충전소의 위치를 전체 리스트에 더해줌
    for i in range(len(charge_station)):
        station_arr[charge_station[i]] += 1

    count = 0           # 충전 횟수
    bus = K             # 버스의 현재 위치
    station_num = 0     # 마지막으로 충전한 위치

    # 버스가 최대 정류장의 길이 만큼 반복문을 실행
    while bus<N:

        # 현재 위치에 충전기가 있을경우
        if station_arr[bus] == 1:
            count += 1              # 충전횟수 +1
            station_num = bus       # 현재 충전한 정류장 번호를 저장해줌
            bus += K                # 버스에 최대 이동거리를 더해줌
        else:
            bus -= 1                # 충전소가 없는 경우 뒤로 1칸 후진

        # 무한루프 돌 경우
        # 반복문을 돌며 station_num에 버스의 이전 위치를 넣어주고
        # bus의 위치를 최대 이동거리 만큼 이동해 주었는데
        # else문을 통해서 이전 station_num와 bus의 위치가 같아졌을 경우
        # 즉 최대 거리로 이동해도 다음 충전소 까지 가지 못할때

        if station_num == bus:
            count = 0
            break
    print(f'#{tc} {count}')


