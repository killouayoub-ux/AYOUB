a=int(input("saisir un entiers strictement positif : "))
b=int(input("saisir un entiers strictement positif : "))
if a>0 and b>0:
    if a%b==0:
        print("a est divisible par b")
    else:
        print("a n'est pas divisible par b")