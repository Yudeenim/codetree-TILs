m1, d1, m2, d2 = map(int, input().split())
A = input()

day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_day_dif = day_of_week.index(A)

def days(m, d):
    day = d
    for i in range(1, m):
        day += days_of_month[i]
    return day

if days(m2, d2) - days(m1, d1) < 7: 
    print(0)
else: 
    print((days(m2, d2) - days(m1, d1) + start_day_dif) // 7)