# grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
# price = []

# for i in range(len(grain_lst)):
#     price.append(grain_lst[i][1])
#     max_price = max(price)
# num_list = price.index(max_price)
# print(grain_lst[num_list])

grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
# grain_dict = dict(grain_lst)            # 리스트 값을 딕셔너리로 형변환
# key = list(grain_dict.keys())           # 딕셔너리의 key값들을 list로 형변환
# value = list(grain_dict.values())       # 딕셔너리의 value 값들을 list로 형변환
# max_idx = value.index(max(value))       # value리스트의 max 값을 가지는 자리를 찾아옴 > index함수이용

# print(key[max_idx])                     # 제일큰 값을 가지는 value에 해당하는 key값을 가져옴
# 제일 비싼애의 index 번호를 알아야 함

grain_lst.sort(key = lambda x : x[1])   # 람다함수 이용하기
print(grain_lst[-1])