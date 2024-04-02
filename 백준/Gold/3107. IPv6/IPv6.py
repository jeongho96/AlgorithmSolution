from sys import stdin

input = stdin.readline

address = list(input().rstrip().split(":"))

# ::로 축약되었을 때
if '' in address:
    miss_part = 8 - (len(address) - 1)
    index = address.index('')
    address[index:index+1] = ['0000'] * miss_part

if len(address) < 8:
    zero = 8 - len(address)
    for _ in range(zero):
        address.insert(address.index(''), '0000')

for i in range(len(address)):
    for j in range(4):
        if len(address[i]) == 4:
            break
        if len(address[i]) < 4:
            address[i] = '0' + address[i]

print(':'.join(address))
