
def countVowels(x):
    vowels="aeiouAEIOU"
    counter=0
    for i in range(0,len(x)):
        if x[i] in vowels:
            counter+=1
    return counter
x= input("enter your name ")
print(countVowels(x))

    