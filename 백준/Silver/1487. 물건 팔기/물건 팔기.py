import sys
n = int(sys.stdin.readline())

cost = []

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    cost.append([temp[0], temp[1]])
    
cost.sort(key = lambda x: (x[0], x[1]))

total = [0] * n

for i in range(n):
    for j in range(i,n):
        benefit = cost[i][0] - cost[j][1]
        if benefit > 0:
            total[i] += benefit
            
result = [cost[i][0] for i in range(n) if total[i] == max(total)]

if sum(total) == 0:
    print(0)
else:
    print(min(result))