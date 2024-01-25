class Student:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

n = int(input())
num = 1
students = []

for _ in range(n):
    height, weight = tuple(map(int, input().split()))
    students.append(Student(height, weight))

students.sort(key = lambda x: (x.height, -x.weight))

for student in students:
    print(student.height, student.weight, num)
    num += 1