def factorial(n):
    if (n > 1):
        return n * factorial(n - 1)
    else:
        return 1
    
def factorial_notation(n):
    sum = 0
    str_n = str(n)
    len_n = len(str_n)
    for index,number in enumerate(str_n):
        sum += int(str_n[index]) * factorial(len_n)
        len_n -= 1
    return sum

import sys

while True:
    T = int(sys.stdin.readline().rstrip())
    if T == 0:
        break
    print(factorial_notation(T))
    