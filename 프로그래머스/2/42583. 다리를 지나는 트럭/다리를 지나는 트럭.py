
from collections import deque


def solution(bridge_length, weight, truck_weights):
    # 초기 설정
    time_count = 0  # 경과 시간
    bridge_queue = deque([0] * bridge_length)  # 다리 상태를 저장하는 큐
    current_weight = 0  # 현재 다리 위의 트럭 무게 합

    while truck_weights or current_weight > 0:  # 대기 트럭이 있거나 다리 위에 트럭이 있을 때
        time_count += 1  # 시간 경과
        # 다리의 맨 앞에 있는 트럭 제거 (다리에서 나감)
        current_weight -= bridge_queue.popleft()

        if truck_weights:  # 대기 트럭이 남아 있다면
            if current_weight + truck_weights[0] <= weight:  # 새로운 트럭이 올라갈 수 있는 경우
                truck = truck_weights.pop(0)
                bridge_queue.append(truck)  # 트럭을 다리 위에 추가
                current_weight += truck  # 현재 다리 위 무게에 트럭 무게 추가
            else:
                bridge_queue.append(0)  # 트럭이 올라갈 수 없으면 0 추가 (시간 경과만 반영)
        else:
            bridge_queue.append(0)  # 대기 트럭이 없을 때는 0 추가 (시간 경과만 반영)

    return time_count
