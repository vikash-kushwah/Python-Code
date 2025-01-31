""" to print a pattern 
        *
       ***
      *****
     *******
    *********         """
t=1
for i in range(1,10,2):
    print(" "*(5-t),"*"*i)
    t=t+1