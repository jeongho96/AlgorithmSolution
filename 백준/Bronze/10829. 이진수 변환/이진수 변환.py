def number2binary(n):
    n = bin(n)
    return n[2:]

n = int(input())
print(number2binary(n))