_ = int(input()) # 3
arr = list(map(int, input().split())) 

new_arr = [elem * elem for elem in arr]

for elem in new_arr:
    print(elem, end=" ")