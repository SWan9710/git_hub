# 문제
# 끝말잇기 단어의 리스트가 주어졌을 때, 몇 번째 사람이 탈락하는지 확인하는 코드를 작성하시오.
# 조건
# 앞서 입력된 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 끝말잇기를 틀리거나 이전에 등장했던 단어를 사용하는 경우, 지게 됩니다.
# 만족하면 탈락
# 1. 앞서 입력된 단어의 마지막 문자가 아니면 탈락
# 2. 이전에 등장했던 단어면 탈락


words = ["round" , "dream", "magnet" , "tweet" , "tweet" , "trick", "kiwi"]
# 처음부터 words의 길이보다 1 작은 위치를 조회 할 때까지 반복
# 마지막 글자는 비교대상이 없기 때문에 그 전까지 조사
duplicated_word = [] # 빈 리스트
idx = 0
while idx < len(words) -1:
    if words[idx][-1] != words[idx+1][0] or words[idx] in duplicated_word:
        print(f'{idx+1} 번째가 탈락하였습니다.')
        break  
    else:
        duplicated_word.append(words[idx])
    idx += 1
    # 조건문을 알맞게 통과하면 idx에 1을 증가시키기
print(duplicated_word)
if len(words)-1 == len(duplicated_word):
    print('아무도 탈락하지 않았습니다.')

# 도전과제
# 반복문 뒤집기
# 끝까지 갔을때 아무도 탈락하지 않았습니다 출력