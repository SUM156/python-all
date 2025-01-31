a=int(input("Enter 1st number to check middle:"))
b=int(input("Enter 2nd number to check middle:"))
c=int(input("Enter 3rd number to check middle:"))
d=int(input("Enter 4th number to check middle:"))
e=int(input("Enter 5th number to check middle:"))
if (a>b and a>c and a>d and a>e)or(a<b and a<c and a<d and a<e):
    print("Oh great this is middle number:",a)
elif (b>a and b>c and b>d and b>e)or(b<a and b<c and b<d and b<e):
   print("Oh great this is middle number:",b)
elif (c>a and c>b and c>d and c>e)or(c<a and c<b and c<d and c<e):
    print("Oh great this is middle number:",c)
elif (d>a and d>b and d>c and d>e)or(d<a and d<b and d<c and d<e):
    print("Oh great this is middle number:",d)
else:
    print("Oh great this is middle number:",e)
