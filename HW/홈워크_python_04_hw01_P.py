# 문제
# 끝말잇기 단어의 리스트가 주어졌을 때, 몇 번째 사람이 탈락하는지 확인하는 코드를 작성하시오.
# 조건
# 앞서 입력된 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 끝말잇기를 틀리거나 이전에 등장했던 단어를 사용하는 경우, 지게 됩니다.

words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
# 처음부터 words의 길이보다 1 작은 위치를 조회 할 때까지 반복
# 마지막 글자는 비교대상이 없기 때문에 그 전까지 조사
duplicated_word = [] # 빈 리스트
idx = 0
while idx < len(words) -1:
    if words[idx][-1] == words[idx +1][0] and words[idx] not in duplicated_word:
        # words 0번째 >> round 의 마지막글자 와 다음글자의 첫번째 글자가 같을때
        # 그리고 지금글자가 이전에 나온글자 중에 없다면 true 로 조건문 통과
        duplicated_word.append(words[idx])
        # 빈 리스트에 현재의 words를 추가해줌
    else: 
        # 조건을 통과하지 못했을 때
        print(f'{idx+1}번째가 탈락했습니다.')
        # 통과하지 못한 글자가 탈락
        break
        # 그리고 반복문 종료
    idx += 1
    # 조건문을 알맞게 통과하면 idx에 1을 증가시키기
print(duplicated_word)

# 도전과제
# 반복문 뒤집기
# 끝까지 갔을때 아무도 탈락하지 않았습니다 출력