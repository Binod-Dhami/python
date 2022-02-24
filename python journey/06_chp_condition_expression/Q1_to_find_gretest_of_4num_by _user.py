a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
c=int(input("enter the num3:"))
d=int(input("enter the num4:"))
if(a>b and a>c and a>d):
    print("a is gretest")
elif(b>c and b>a and b>d):
    print("b is gretest")  
elif(c>a and c>b and c>d):
    print("c is gretest") 
else:
    print("d is gretest")     