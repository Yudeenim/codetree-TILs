arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))

cnt = 1
sum_val = 0
for i in range(4):
    for j in range(cnt):
        sum_val += arr[i][j]
    cnt += 1

print(sum_val)