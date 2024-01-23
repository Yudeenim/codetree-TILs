arr = list(map(int, input().split()))
sum_val = 0
cnt = 0

for elem in arr:
    if elem == 0:
        break
    sum_val += elem
    cnt += 1

print(f"{sum_val} {sum_val / cnt:.1f}")