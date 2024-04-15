N = int(input())  # 사진틀의 개수
M = int(input())  # 총 추천 횟수
recommendations = list(map(int, input().split()))

from collections import defaultdict

# 추천 수와 등록 시간을 기록
photo_frames = []  # (추천 수, 등록 시간, 후보)
photo_dict = defaultdict(lambda: [0, -1])  # 후보의 추천 수와 등록 시간

time = 0
for rec in recommendations:
    if photo_dict[rec][1] != -1:
        # 이미 사진틀에 있으면 추천 수만 증가
        for i, frame in enumerate(photo_frames):
            if frame[2] == rec:
                photo_frames[i] = (photo_frames[i][0] + 1, photo_frames[i][1], rec)
                break
    else:
        if len(photo_frames) >= N:
            # 사진틀이 꽉 찼을 때, 최소 추천 수, 가장 오래된 사진을 제거
            photo_frames.sort()  # 추천 수, 등록 시간 순으로 정렬
            removed = photo_frames.pop(0)
            photo_dict[removed[2]] = [0, -1]  # 사진틀에서 제거
        # 새 사진 추가
        photo_frames.append((1, time, rec))
        photo_dict[rec] = [1, time]

    time += 1

# 결과 출력
photo_frames.sort(key=lambda x: x[2])  # 후보 번호 기준으로 정렬
print(' '.join(str(frame[2]) for frame in photo_frames))
