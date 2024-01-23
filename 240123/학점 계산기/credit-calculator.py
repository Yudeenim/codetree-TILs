n = int(input())
arr = list(map(float, input().split(" ")))

summ = sum(arr)
avg = summ / n

print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")