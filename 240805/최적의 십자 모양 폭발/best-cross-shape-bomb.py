n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def bomb(grid, i, j):
    num = grid[i][j]
    for k in range(1, num):
        if i - k >= 0:
            grid[i - k][j] = 0
        if i + k < n:
            grid[i + k][j] = 0
        if j - k >= 0:
            grid[i][j - k] = 0
        if j + k < n:
            grid[i][j + k] = 0
    grid[i][j] = 0

def apply_gravity(grid):
    for j in range(n):
        stack = []
        for i in range(n):
            if grid[i][j] != 0:
                stack.append(grid[i][j])
        for i in range(n - 1, -1, -1):
            if stack:
                grid[i][j] = stack.pop()
            else:
                grid[i][j] = 0

def count_pairs(grid):
    pairs = 0
    for i in range(n):
        for j in range(n):
            if i < n - 1 and grid[i][j] == grid[i + 1][j] and grid[i][j] != 0:
                pairs += 1
            if j < n - 1 and grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                pairs += 1
    return pairs

def clone_grid(grid):
    return [row[:] for row in grid]

max_pairs = -1
best_i, best_j = 0, 0

for i in range(n):
    for j in range(n):
        if grid[i][j] > 0:  
            temp_grid = clone_grid(grid)
            bomb(temp_grid, i, j)
            apply_gravity(temp_grid)
            pairs = count_pairs(temp_grid)
            if pairs > max_pairs:
                max_pairs = pairs
                best_i, best_j = i, j

print(max_pairs)