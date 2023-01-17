# 1. 항구 정보를 리스트로 표현
ports = ['F','F','F','T','F','F','F','T','T','F','F','F','F','F','T',]
#1 ~ 15까지의 항구 리스트 생성
# count = 0
# for no in ports:
#     count += 1
#     if no == 'F':
#         print(count,False)
#     else:
#         print(count,True)
count = 0
for no in ports:
    count += 1
    if count % 2 == 1:
        if no == 'F':
            print(count,False)
        else:
            print(count,True)



