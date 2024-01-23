n = int(input())
nums = list(map(int, input().split()))

max_num = -1

for curr_num in nums:
    if max_num < curr_num:
        count = 0
        for elem in nums:
            if elem == curr_num:
                count += 1
        if count == 1:
            max_num = curr_num

print(max_num)