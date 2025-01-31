f=open('C:\\Users\\vikash\\OneDrive\\Desktop\\practice\\I3 practice\\file_inPy.py') 
for i in f:
    if "lokesh" in i:
        print(i)
    elif "vikash" in i:
        print(i)
    
f=open('C:\\Users\\vikash\\OneDrive\\Desktop\\practice\\I3 practice\\file_inPy.py')
t=[i.strip().upper() for i in f if "lokesh" in i]

sum=0
print(t)



