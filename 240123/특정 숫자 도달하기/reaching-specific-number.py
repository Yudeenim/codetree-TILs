arr = list(map(int, input().split(" ")))
summ = 0
avg = 0

i = 0

while arr[i] < 250:
    summ += arr[i]
    i += 1

avg = summ / i
print(summ, avg)