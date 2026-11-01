a1=int(input("l'age de la premiere personne est : "))
a2=int(input("l'age de la deuxieme personne est : "))
a3=int(input("l'age de la troisieme personne est : "))
if a1>=a2 and a1>=a3:
    print("le premier age est le plus agé : ")
elif a2>=a1 and a2>=a3:
    print("le deuxieme age est le plus agé : ")
else:
    print("le troisieme age est le plus agé : ")