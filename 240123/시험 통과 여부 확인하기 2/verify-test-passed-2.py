n = int(input())
pass_people = 0

for _ in range(n):
	arr = list(map(int, input().split()))
	sum_val = sum(arr)
	avg = sum_val / 4
	
	if avg >= 60:
		print("pass")
		pass_people += 1
	else:
		print("fail")

print(pass_people)