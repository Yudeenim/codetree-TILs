A = list(input())
min_num = 20

def count_str(arr):
    count = 1
    letter = arr[0]
    result = []
    for i in range(1, len(arr)):
        if arr[i] == letter:
            count += 1
        else:
            result.append(f"{letter}{count}")
            letter = arr[i]
            count = 1
    result.append(f"{letter}{count}")
    return result

for i in range(len(A)):
    current_length = len(''.join(count_str(A)))
    min_num = min(min_num, current_length)
    temp = A[len(A)-1]
    for j in range(len(A)-1, 0, -1):
        A[j] = A[j-1]
    A[0] = temp

print(min_num)