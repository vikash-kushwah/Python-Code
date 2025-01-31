# to print the character, distinct character, and length in list 
l=[]
name="abhcksbd"
for i in name:
    print(i)
    if i not in l:
        l.append(i)

print(l)
print(len(l))