n=int(input("donner un entier naturel strictement positif : "))
if n>0:
    s=0
    for i in range(1,n+1):
        s=s+(1/i)
    print(format(s,".2f"))
else:
    print("le nombre n'a partient pas à N*.")