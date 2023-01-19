# fn_d(91) 
# 출력 예시 
# 101

def fn_d(n):
    n = str(n)# 입력받은 n 값을 문자열로 변환
    result_list = ''.join(n) # 입력받은 값에 공백을 추가해서 리스트에 넣어줌
    num = 0
    for i in range(len(result_list)): #임시변수 i 값이 result_list의 길이만큼 돌림 
                                        # 두자리이면 리스트의 길이가 [0][1] 이니까 두번 돌림
        num += int(result_list[i]) #result_list[0]의 값을 int 형식으로 바꿔서 num에 넣어줌
    n = int(n) #입력 받았던 n값을 다시 int 형식으로 변환
    num += n # num 값에 추가로 n값을 넣어줌
    return num # 총 num값을 반환

print(fn_d(1))
# 셀프넘버를 찾기위해 fn_d(n) 함수를 입력받은 n값만큼 반복
# 셀프넘버의 범위 조건이 is_selfnumber 보다 작은수가 자릿수 + 본인을 했을때 is_selfnumber이 나와야 함
# 범위조건을 입력받은 n값만큼 돌려도 결과를 출력하기에 충분함
# 범위조건을 다 돌아도 is_selfnumber 값이 안나온다면 셀프넘버임
def is_selfnumber (n) :
    for i in range(n) : # i를 n만큼 돌림
        if fn_d(i) == n : # fn_d(i) -> 0 부터 n까지의 함수실행 결과값과 n 값을 비교
                            # 실행 결과값이 있다면 비교과 되고 없다면 else 문으로 넘어감
            return '셀프넘버가 아닙니다.'
    else :
        return '셀프넘버 입니다.'

print(is_selfnumber(50))
