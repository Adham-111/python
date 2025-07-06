def countString (x):
    for i in range(0,len(x)) :
        if x[i] == "i" :
            return i
        else :
            continue
x=input("enter a string ")
indexI= countString(x)
print(indexI)
        