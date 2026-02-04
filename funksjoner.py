    
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

print(f"REKTANGLET HAR AREAL PÅ {rektangel()}")

num1 = ""
while num1 == "":
    try:
        num1 = input("Please give us a chance...").strip()
        num1 = int(num1)
    except ValueError:
            print(f"{num1} isn't a whole number, just give us a chance")
            num1 = ""
num2 = ""
while num2 == "":
    try:
        num2 = input("AND THE SECOND ONE, PLEASE!").strip()
        num2 = int(num2)
    except ValueError:
            print(f"PLEASE JUST MAKE {num2} A WHOLE NUMBER PLEASE")
            num2 = ""

if num1 > num2:
    print(f"Well God, {num1} is bigger!")
elif num2 > num1:
    print(f"Well God, {num2} is bigger!")
else:
    print("They're the same!")