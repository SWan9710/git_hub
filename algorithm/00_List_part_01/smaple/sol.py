import sys
# open함수의 인자로 들어가는
# 문자열은 내가 열고자 하는 파일의 '경로'와 이름입니다.
sys.stdin=open('input.txt')

N = int(input())
print(N)

# map의 첫번째 인자는 함수
# 두번째 인자는 순회 가능한 요소
# 순회 가능한 요소가 가진 각 값들을 첫뻔째 인자에 작성한 함수에 대입하여 실행
# 실행한 결과를 모아서 map Object로 반환
arr = list(map(int, input().split()))
print(arr)