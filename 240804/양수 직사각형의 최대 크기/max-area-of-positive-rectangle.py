n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
result = 0

def in_grid(x, y, i, j):
    return x >= 0 and y >= 0 and x + j < m and y + i < n

def is_pos(x, y, i, j):
    for k in range(j + 1):
        for l in range(i + 1):
            if grid[y + l][x + k] < 0:
                return False
    return True

def simulation(x, y):
    global result
    for k in range(n - y):
        for l in range(m - x):
            if in_grid(x, y, k, l) and is_pos(x, y, k, l):
                result = max(result, (k + 1) * (l + 1))

for a in range(n):
    for b in range(m):
        simulation(b, a)

print(result)