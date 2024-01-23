arr_2d = [
	list(input().split())
	for _ in range(5)
]

for i in range(5):
	for j in range(3):
		arr_2d[i][j] = arr_2d[i][j].upper()
		print(arr_2d[i][j], end=" ")
	print()