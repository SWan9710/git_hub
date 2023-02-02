import sys
sys.stdin=open('input.txt')
# 버블정렬

# 최초 배열 길이에서 -1 한만큼 비교해줄거
# 만약 배열 길이가 5면 4부터 시작
arr = list(map(int, input().split()))
for i in range(len(arr)-1,0,-1):
    # i = 4, j는 0,1,2,3 들어감
    for j in range(i):
        # 비교해줄때 i에 5값이 들어가면 j가 가져오는 값이 배열의 길이를 벗어남
        # 그래서 최초에 들고오는 i의 값에서 -1을 해줘서 j의 길이를 맞춰주는거
        if arr[j] > arr[j+1]:
            # 만약 j = 0 값이 j = 1값보도 클 경우 서로의 위치를 교환
            arr[j], arr[j + 1] = arr[j+1], arr[j]
            print(arr)






