arr = list(map(int, input().split()))
n = 0

for elem in arr:
    if elem == 0:
        break
    n += 1

for i in  range(n-1, -1, -1):
    print(arr[i], end = " ")