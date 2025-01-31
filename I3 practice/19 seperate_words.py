# enter string and seperate the different words

words= input("enter the sentences: ")
l=words.split()
print(l)
l_list=[]
for i in l:
    if i not in l_list:
        l_list.append(i)
print(l_list)