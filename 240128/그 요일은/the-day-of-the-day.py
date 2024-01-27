m1, d1, m2, d2 = map(int, input().split())
A = input()

days = 0
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 시작 날짜의 요일을 계산
start_day_index = day_of_week.index(A)
d1 += start_day_index

while True:
    if m1 == m2 and d1 >= d2:
        if d1 == d2:
            days += 1
        break

    days += 1
    d1 += 7

    if d1 > day_of_month[m1]:
        m1 += 1
        d1 = d1 - day_of_month[m1]

print(days)