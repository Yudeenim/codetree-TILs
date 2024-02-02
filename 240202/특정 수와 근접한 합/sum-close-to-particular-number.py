n, s = tuple(map(int, input().split()))
n_arr = list(map(int, input().split()))
new_arr = n_arr.copy()
diff = 10000

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        new_arr = [elem for k, elem in enumerate(new_arr) if k not in (i, j)]
        if abs(sum(new_arr) - s) < diff:
            diff = abs(sum(new_arr) - s)
        new_arr = n_arr.copy()

print(diff)