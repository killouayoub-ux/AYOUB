a=float(input("donner la valeur de a: "))
b=float(input("donner la valeur de b: "))
c=float(input("donner la valeur de c: "))
if a==0 and b==0 and c==0:
    print("l'equation a une infinité de solutions")
    if a==0 and b==0 and c!=0:
        print("l'equation n'a pas de solution")
    elif a==0 and b!=0:
        print("l'equation a une solution unique x=", -c/b)
elif a!=0:
    D=b**2-4*a*c
    if D>0:
        x1=(-b+D**0.5)/(2*a)
        x2=(-b-D**0.5)/(2*a)
        print("l'equation a deux solutions x1=", x1, "et x2=", x2)
    elif D==0:
        x=-b/(2*a)
        print("l'equation a une solution unique x=", x)
    else:
        print("l'equation n'a pas de solution")