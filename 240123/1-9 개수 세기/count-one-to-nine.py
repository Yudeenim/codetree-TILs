n = int(input())

arr = list(map(int, input().split()))
count_arr = [0] * 10

for elem in arr:
	count_arr[elem] += 1
	
for i in range(1, 10):
	print(count_arr[i])