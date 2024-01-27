m1,d1,m2,d2=tuple(map(int,input().split()))
sumval=0
cnt=0
day=input()
def mcal(m):
    if (m>=8 and m%2==0) or (m<8 and m%2 !=0):
        return 31
    elif (m==2):
        return 29
    else:
        return 30

if (m1<m2) or (m1==m2 and (d2>=d1)):
    for i in range(m1,m2):
        sumval += mcal(i)
    total = sumval+d2-d1
    arr=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    arrr=[0,0,0,0,0,0,0]
    for i in range(total+1):
        arrr[i%7] +=1
    for i in range(7):
        if arr[i]==day:
            cnt = i
    print(arrr[cnt])

else:
    print("0")