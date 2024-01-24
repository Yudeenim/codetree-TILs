n = int(input())
arr = list(map(int, input().split()))
new_arr = []
middle_arr = []

for i in range(n):
    new_arr.append(arr[i])
    new_arr.sort()

    if (i + 1) % 2 == 1:
        middle_index = i // 2
        middle_arr.append(new_arr[middle_index])

for elem in middle_arr:
    print(elem, end = " ")