L=float(input("la longeur du rectangle est : "))
l=float(input("la largeur du rectangle est : "))
if l>L:
    print("impossible")
elif L==l:
    print("s'agit d'un carré")
else:
    print("s'agit d'un rectangle non carré")