n=float(input("saisir votre note : "))
if n>=0 and n<10:
    print("echec")
elif n>=10 and n<12:
    print("passable")
elif n>=12 and n<14:
    print("assez bien")
elif n>=14 and n<16:
    print("bien")
elif n>=16 and n<=20:
    print("tres bien")
