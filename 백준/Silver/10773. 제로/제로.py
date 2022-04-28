k = int(input())
list1 = []
for i in range(k):
    number = int(input())
    if number == 0:
        list1.pop()
    else:
        list1.append(number)

print(sum(list1))