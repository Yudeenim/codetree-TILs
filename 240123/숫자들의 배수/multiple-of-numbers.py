n = int(input())
num = 1
cnt = 0
arr = []

while(1):
    arr.append(n * num)
    if (n * num % 5 == 0):
        cnt += 1
    num += 1
    if cnt == 2:
        break

print(*arr)