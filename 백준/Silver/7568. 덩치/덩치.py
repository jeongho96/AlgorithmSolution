# 덩치(7568번)
n = int(input())
m = []
list1 = []
for i in range(n):
    x,y = map(int,input().split())
    list1.append((x,y))

for i in range(n):
    count = 0
    for j in range(n):
        if list1[i][0] < list1[j][0] and list1[i][1] < list1[j][1]:
            count += 1 
    m.append(count + 1) 
 
for d in m:
    print(d,end=" ")