sample_list = [11 , 22 , 33 , 55 , 66]
# 주어진 리스트의 3번째 자리에 있는 항목을 제거하고 변수에 할당해 주세요.

x = sample_list.pop(3)
# print(x)
# print(sample_list)

# 주어진 sample_list의 가장 뒤에 77를 추가해 보세요
sample_list.append(77)
# print(sample_list)

# 할당해놓은 변수의 값을 sample_list의 2번 인덱스에 추가해 보세요.
sample_list.insert(2,x)
# print(sample_list)

my_tuple = (11,22,33,44,55,66,)
# print(my_tuple)
# 주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당해보세요
new_tuple = my_tuple[3:5]
# print(new_tuple)

# lambda 예제
test_list = [1,2,3,7,4,6,5]
test_list.sort()
# print(test_list)

scores = [('eng',88),('sci',90),('math',80)]
def check(x):
    return x[1]

scores.sort(key=check)
scores.sort(key=lambda x: x[1])
print(scores)
