n = int(input())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

if (arr_A.sort() == arr_B.sort()): print ("Yes")
else: print("No")