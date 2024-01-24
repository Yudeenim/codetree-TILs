n = int(input())

arr = list(map(int, input().split()))
arr1 = sorted(arr)
arr2 = arr1[::-1]

print(*arr1)
print(*arr2)