L = int(input())
str1 = input()
r = 31
M = 1234567891
result = 0
for i in range(L):
    result += ((ord(str1[i])- 96) * r ** i)
print(result % M)
