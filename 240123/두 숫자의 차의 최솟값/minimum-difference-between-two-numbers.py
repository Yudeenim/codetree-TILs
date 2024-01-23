n = int(input())
arr = list(map(int, input().split()))
min_dif = 99

for i in range(len(arr)):
    for j in range(len(arr)):
        if (arr[i] - arr[j]) > 0 and (arr[i]-arr[j]) <min_dif:
            min_dif = arr[i]-arr[j]
        elif (arr[i] - arr[j])< 0 and -(arr[i] - arr[j]) < min_dif:
            min_dif = -(arr[i] - arr[j])
        elif (arr[i] - arr[j]) == 0:
            continue

print(min_dif)