x=int(input("saisir un entier naturel : "))
n=int(input("saisir un entier naturel : "))
if x>=0 and n>=0:
    s=1
    for i in range(n):
        s*=x
    print("x=",s)