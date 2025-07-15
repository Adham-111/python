def validemail(x):
    if x and "@" in x :
        parts=x.split("@")
        domain=parts[1]
        name=parts[0]
        try:
            if "@" not in domain:
             return True
        except: 
            print("you enter more than @ in email")
            
        if len(domain)!= 0 and len(name)!= 0 and "." in domain :
            domainparts=domain.split(".")
            part1_domain=domainparts[0]
            if part1_domain :
                return True
            else:
                return False
        else: 
            return False
            
    else :
          return False  
def validationName (x):
    if x and  x.isdigit :
        return True
    else :
        return False
x=input("enter your name ")
valid=validationName(x)
if valid :
     while True:
        email= input("enter your email ")
        if validemail(email):
            print(f"your name is {x} and your email : {email}")
            break
        else:
            print("invalid email please enter a valid email")
        
else :
    print("invalid name ") 


        
    