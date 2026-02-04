    
def rektangel():
    bredde = ""
    while bredde == "":
        try:
            bredde = input("VENNLIGST TAST INN BREDDE: ").strip()
            bredde = int(bredde)
        except ValueError:
                print(f"{bredde} ER IKKE ET HELTALL, PRØV IGJEN")
                bredde = ""
    lengde = ""
    while lengde == "":
        try:
            lengde = input("VENNLIGST TAST INN LEGNDE: ").strip()
            lengde = int(lengde)
        except ValueError:
                print(f"{lengde} ER IKKE ET HELTALL, PRØV IGJEN")
                lengde = ""
    return(lengde * bredde)

def checkNum():
    n1 = ""
    while n1 == "":
        try:
            n1 = input("VENNLIGST TAST INN TALL 1 ").strip()
            n1 = int(n1)
        except ValueError:
                print(f"{n1} ER IKKE ET HEL TALL, PRØV IGJEN")
                n1 = ""
    n2 = ""
    while n2 == "":
        try:
            n2 = input("VENNLIGST TAST INN TALL 2 ").strip()
            n2 = int(n2)
        except ValueError:
                print(f"{n1} ER IKKE ET HEL TALL, PRØV IGJEN")
                n2 = ""
    if n1 > n2:
        return(n1)
    elif n2 > n1:
        return(n2)
    else:
        return("BEGGE")


print(f"REKTANGLET HAR AREAL PÅ {rektangel()}")
print(f"{checkNum()} ER DET STØRSTE TALLET")