x = int(input("Enter the number :"))
for n in range(2,x):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            a=1
            flag=1
            break
    if flag==0:
         print(n, end=" ")
