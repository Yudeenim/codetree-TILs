n = input()
arr = list(map(int, input().split(" ")))
new_arr = []

for elem in arr:
    new_arr.append(elem * elem)

print(*new_arr)