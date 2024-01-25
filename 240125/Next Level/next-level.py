class Id_Level:
    def __init__(self, ID, level):
        self.ID = ID
        self.level = level
    
User1 = Id_Level("codetree", 10)
x = list(map(str, input().split()))
x[1] = int(x[1])
User2 = Id_Level(x[0], x[1])

print(f"user {User1.ID} lv {User1.level}")
print(f"user {User2.ID} lv {User2.level}")