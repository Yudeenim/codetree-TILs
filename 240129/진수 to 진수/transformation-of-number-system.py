a, b = tuple(map(int, input().split()))
n = input()
n = [int(digit) for digit in str(n)]
digits = []
num = 0

for i in range(len(n)):
    num = num * a + n[i]

while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % b)
    num //= b

print(int(''.join(map(str, digits[::-1]))))