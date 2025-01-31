def pow(a,b=2):
    return a**2

def sum(a:int,b:int):              ### :_____ is used to define the type of data and it is optional.
    return a+b

print(pow(5), "my",sep="-------")  ### sep="  " is used to seprate the output in same line 
print(pow(6),end="#####")          ### end="  " is used to define the end of line of output
print(pow(7))