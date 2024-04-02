

from sys import stdin

input = stdin.readline

address = list(input().rstrip().split(":"))

# ::로 축약되었을 때
if '' in address:
    miss_part = 8 - (len(address) - 1)
    index = address.index('')
    address[index:index+1] = ['0000'] * miss_part


for i in range(len(address)):
    address[i] = address[i].zfill(4)

print(':'.join(address))
