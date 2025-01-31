#program for finding maximum inside list 

list=[["ram",89],["lokesh",45],["rav",99],["govind",100],["rajesh",65]]
a=0
for i in list:
    if i[1]>=a:
        a=i[1]
print("maximum number is :",a)

#for adding city in list
for k in range(len(list)):
    z=input("enter name of city :")
    list[k].append(z)
print(list)

# for removing marks of list 
for k in range(len(list)):
    p=list[k]
    p.pop(1)      ###here  we can also use ------- p.remove(p[1]) 
print(list)

