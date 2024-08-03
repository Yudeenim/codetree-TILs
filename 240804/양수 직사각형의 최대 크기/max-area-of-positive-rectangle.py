n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
result = 0

def in_grid (x, y, i, j):
    if x >= 0 and y >= 0 and x + j <= n and y + i <= m:
        return True
    else: return False

def is_pos (x, y, i, j):
    for k in range(x+1):
        for l in range(y+1):
            if grid[y+l][x+k] < 0:
                return False
            else: return True


def simulation (x, y):
    global result
    for k in range(n):
        for l in range(m):
            if in_grid(x, y, k, l) and is_pos(x, y, k, l):
                result = max(result, (k+1)*(l+1))

for a in range(1, n):
    for b in range(1, m):
        simulation(a, b)

print(result)