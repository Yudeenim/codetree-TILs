n = int(input())
arr = list(map(int, input().split()))
arr2 = []
cnt = 0

for elem in arr:
    if elem %2 == 0:
        arr2.append(elem)
        cnt += 1
for i in range(cnt - 1, -1, -1):
    print(arr2[i], end = " ")