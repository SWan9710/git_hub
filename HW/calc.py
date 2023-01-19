
def add(x, y):
    result = x + y
    return result

def sub(x, y):
    result = x - y
    return result

def mul(x, y):
    result = x * y
    return result
    

def div(x, y):
    try :
        result = x / y
        return result
    
    except ZeroDivisionError:
        return '0으로는 나눌수 없습니다.'