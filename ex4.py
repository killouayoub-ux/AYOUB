n=int(input("donner un entier naturel : "))
s=0
for i in range(1,((n//2)+1)):
    if n%i==0:
        s=s+i
if s==n:
    print("le nombre est parfait")
else:
    print("le nombre n'est pas parfait")