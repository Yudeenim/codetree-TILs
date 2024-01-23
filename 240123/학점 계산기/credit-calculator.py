n = int(input())
arr = list(map(float, input().split(" ")))
summ = 0
avg = 0

for elem in arr:
    summ += elem

avg = summ / n

print(f"{avg:.1f}")

if avg >= 4:
    print("Perfect")
elif avg >= 3:
    print("Good")
else:
    print("Poor")