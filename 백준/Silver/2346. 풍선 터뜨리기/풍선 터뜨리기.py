N = int(input())
balloons = list(map(int, input().split()))

result = []
index = 0
length = N

for _ in range(N):
    result.append(str(index + 1))
    move = balloons[index]
    balloons[index] = 0  # 현재 풍선을 터뜨림
    
    if _ < N-1:  # 마지막 풍선이 아니라면
        if move > 0:
            while move > 0:
                index = (index + 1) % length
                if balloons[index] != 0:
                    move -= 1
        else:
            while move < 0:
                index = (index - 1 + length) % length
                if balloons[index] != 0:
                    move += 1

print(' '.join(result))
