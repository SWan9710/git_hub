def check(input_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in input_str:
        if char.isalpha():          # 입력받은 문자가 글자일 경우 isalpha로 비교
            char_count += 1         # char_count에 += 1
        elif char.isdigit():        # 입력받은 문자가 숫자일 경우 isdigit로 비교
            digit_count += 1
        else:
            symbol_count += 1       # 문자와 숫자 모두 아닐경우 기호로 판단
    
    return char_count, digit_count, symbol_count
input_str = 'adasldkjalsjieawe1239054#!@$@$TWSDFA!$ASDfg'
char_count, digit_count, symbol_count = check(input_str) # 입력받은 인풋값을 각각 하나에 할당
print(check(input_str))

