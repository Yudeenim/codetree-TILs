arr = list(map(int, input().split()))
new_arr = []

for i in range(100):
	if arr[i] == 0:
		break
	if arr[i] % 2 == 0:
		new_arr.append(arr[i] // 2)
	else:
		new_arr.append(arr[i] + 3)

for elem in new_arr:
	print(elem, end=" ")