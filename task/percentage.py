a=int(input("Enter 1st number to check middle:"))
b=int(input("Enter 2nd number to check middle:"))
c=int(input("Enter 3rd number to check middle:"))
d=int(input("Enter 4th number to check middle:"))
e=int(input("Enter 5th number to check middle:"))
Total=a+b+c+d+e
percent=(Total/500)*100
print("total marks=",Total,"percentage=",percent)
if percent>=85:
    print("My dear sudent you have got A1 grade:")
elif percent>=80:
    print("My dear sudent you have got A grade:")
elif percent>=75:
    print("My dear sudent you have got B+ grade:")
elif percent>=70:
    print("My dear sudent you have got B grade:")
elif percent>=60:
    print("My dear sudent you have got C grade:")
elif percent>=50:
    print("My dear sudent you have got D grade it is not good grade to your study so please you can improvt your Exams:")
else:
    print("This is very bad for you because you have got suply:")
