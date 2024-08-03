n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
result = 0

def in_grid(x, y, i, j):
    return x >= 0 and y >= 0 and x + j <= m and y + i <= n

def is_pos(x, y, i, j):
    for k in range(i):
        for l in range(j):
            if grid[y + k][x + l] < 0:
                return False
    return True

def simulation():
    global result
    for x in range(m):
        for y in range(n):
            for i in range(1, n - y + 1):
                for j in range(1, m - x + 1):
                    if in_grid(x, y, i, j) and is_pos(x, y, i, j):
                        result = max(result, i * j)

simulation()
print(result)