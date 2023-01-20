def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))

def sum(n):
    if n == 5:
        return True
    else:
        return sum(n+1)
print(sum(0))