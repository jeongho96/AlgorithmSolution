from sys import stdin

input = stdin.readline

N = int(input().rstrip())

position_list = list(map(int, input().rstrip().split()))
# 압축 기준이 되는 값을 만들기 위해서
# 중복을 제거하고, 정렬 수행.
comp_position = sorted(set(position_list))
answer_list = []

# 시간 초과 발생
# # comp_position에 그 값의 인덱스가 곧 압축한 좌표 값.
# for i in position_list:
#     answer_list.append(comp_position.index(i))

# comp_position의 각 값과 인덱스를 매핑하는 딕셔너리 생성
# 이렇게 하면 각 값의 인덱스를 빠르게 찾을 수 있음
position_to_index = {value: index for index, value in enumerate(comp_position)}

answer_list = [position_to_index[value] for value in position_list]

print(*answer_list, sep=' ')
