# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 
def de_identify(personal_number):
    # 문자열이 가진 특성상 원본을 바꿀수는 없으니 변경되 값을 반환
    personal_number.replace('-','') 
    return personal_number[:6] + '*'*7
    

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))


