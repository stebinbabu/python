a=int(input("Enter the limit:"))
for i in range(1,a):
    for j in range(1,i+1):
        print("*",end="")
    print("\n")
for i in range(a,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("\n")