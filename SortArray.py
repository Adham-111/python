def sortllist (x) :
    ascending_order=sorted(x)
    descending_Order=sorted(x,reverse=True)
    return ascending_order , descending_Order

number=[]    
for i in range(5):
    x=int(input("enter a number :"))
    if x :
        number.append(x)
print(number)        
print(sortllist(number))