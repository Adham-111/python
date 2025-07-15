def GenerateMario (x):
    l=x 
    for i in range(x+1):
        print(" "*l+i*"*")
        l-=1
x=int(input("enter a number:"))
GenerateMario(x)        
