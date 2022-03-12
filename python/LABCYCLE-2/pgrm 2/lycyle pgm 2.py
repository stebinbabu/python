lst = []
n = int(input("enter the limit"))
print("enter the elements")
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)
result = []
over =[]
for i in lst:
    if i > 100:
        over.append(i)
    else:
        result.append(i)
print("under 100 ",result)
print("over 100", over)