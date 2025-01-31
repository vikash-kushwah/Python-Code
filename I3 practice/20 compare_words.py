#comparing the words between two sentences

p='''i am in Jaipur 
where do you live
i am studying in btech
'''
q='''my name is sahil 
i am from hariyana 
and you'''

l=p.split()
m=q.split()
c_list=[]
for i in l:
    if i in m:
        if i not in c_list:
            c_list.append(i)
print(c_list)            

 