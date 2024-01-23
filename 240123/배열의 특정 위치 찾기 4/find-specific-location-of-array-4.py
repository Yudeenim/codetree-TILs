arr = list(map(int, input().split()))
sum_val = 0
cnt = 0

for elem in arr:
    if elem == 0:
        break
    elif elem % 2 == 0:
        cnt += 1
        sum_val += elem

print(cnt, sum_val)