current=int(input("enter the current year"))
final=int(input("enter the final year"))
print("leap years are :")
for year in (range(current,final)) :
        if(year%4==0) and (year%100!=0) or (year%400==0) :
                    print(year,"year")