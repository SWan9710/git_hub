# 함수가 하는 가장 중요한 역할
# code block에 작성된 특정한 로직을 `호출시마다` 실행하는데 있다.
# 만약 그 결괄를 반환해야 한다면,
# return 뒤에는 표현식이 올 수 있고,
# 반드시 하나의 객체만 반환하여야 하는데,
# 만약 2개 이상의 객체를 반환하려고 한다며? -> 튜플로 묶어서 반환한다.
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y
    
# 단, 0으로 나눌시, 0으로는 나눌 수 없습니다. 라는 문자 출력해야한다.
def div(x, y):
    try :
        return x / y
    
    except ZeroDivisionError:
        return '0으로는 나눌수 없습니다.'