def domain(x):
    domains=map(lambda x: x.split("@")[1],x)
    return list(domains)
y=["adham@gmail.com","ali@gmail.com","adham@yahoo.com"]
print(domain(y))
