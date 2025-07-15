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
x=input("enter your email ")
print(validemail(x)) 

