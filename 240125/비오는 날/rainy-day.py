n = int(input())
class data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

datas = []
for _ in range(n):
    datas.append(list(input().split()))
datas.sort()

for row in range(n):
    if datas[row][2] == 'Rain':
        print (*datas[row])
        break