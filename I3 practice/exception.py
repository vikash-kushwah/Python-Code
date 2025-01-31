def mydc(fx):
    def Mfx():
        print("-"*30)
        fx()
        print("-"*30)
    return Mfx
    
@mydc
def displaymsg():
    print("Arvind Mehta")

@mydc
def echolist():
    for i in range(10):
        print(i,end=" ")
    print()
    

    
displaymsg()
echolist()

def mydcs(fx):
    def Mfxs(*args,**kwargs):  #we also use def Mfxs(*args):   *args- used for list and **kwargs-used for dictionary
        print("-"*30)
        fx(*args,**kwargs)
        print("-"*30)
    return Mfxs

@mydcs
def sum(a,b):
    print(a+b)
@mydcs
def diff(a,b):
    print(a-b)

sum(8,9)
diff(6,4)

#exception in python include try except else and finally

a,b=10,5
l=[10,20]
i=0
try:
    print(l[i]/b)
except ZeroDivisionError:
    print("don't enter 0")
except IndexError:
    print("index must be between 0-1")
except:
    print("Error")
else:
    print("code is running")
finally:
    print(a+10)