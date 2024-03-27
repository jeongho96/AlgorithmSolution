def day_of_week(x, y):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # x월 y일까지의 경과 일수 계산
    days_passed = sum(month_days[:x-1]) + y - 1
    return days[days_passed % 7]

# 입력 받기
x, y = map(int, input().split())

# 요일 출력
print(day_of_week(x, y))