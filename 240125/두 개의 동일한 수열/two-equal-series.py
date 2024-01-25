n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def equal():
    for elem1, elem2 in zip(a, b):
        if elem1 != elem2:
            return False
    
    return True

a.sort()
b.sort()

if equal():
    print("Yes")
else:
    print("No")