a=int(input("enter the coefficient of x**2: "))
b=int(input("enter the coefficient of x: "))
c=int(input("enter the constant: "))
d=(b**2)-(4*a*c)
if d>=0:
    x=(-b+(d**(1/2)))/(a*2)
    y=(-b-(d**(1/2)))/(a*2)
    print(x,y)
    
else:
    print("roots of quadratic equation is imaginary")
    
    
