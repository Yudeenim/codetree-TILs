n = int(input())
arr = [1, n]
cnt = 1

while True:
	cnt += 1
	arr.append(arr[cnt - 1] + arr[cnt - 2])
	if arr[cnt] > 100:
		break

for elem in arr:
	print(elem, end=" ")