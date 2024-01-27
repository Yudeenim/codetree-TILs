#m1월 d1일이 월요일, + 7일마다 월요일. 다음 달로 넘어가는 경우, +7 후 남는 day를 다음 달로 옮기기(- 달의 마지막 날.)

m1, d1, m2, d2 = map(int, input().split())
A = input()

days = 0
day_of_week = ["0", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(8):
    if day_of_week[i] == A:
        d1 += (i - 1)

while True:
    if m1 == m2 and d1 >= d2:
        if d1 == d2:
            days += 1
        break

    days += 1                       #요일이 몇 번인지
    d1 += 7                         #d1에서 7일을 늘려 요일 계산

    if d1 > day_of_month[m1]:
        m1 += 1
        d1 = d1 - day_of_month[m1]
       
print(days)