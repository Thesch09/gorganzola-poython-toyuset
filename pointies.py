from rich import print
score = -10000000

def add():
    n1 = ""
    while n1 == "":
        try:
            print("[green]VENNLIGST SKRIV INN HVOR MANGE POENG DU VIL LEGGE INN I KONTOEN")
            n1 = input("").strip()
            n1 = int(n1)
            return(n1)
        except ValueError:
                print(f"[red]{n1} ER IKKE ET HEL TALL, PRØV IGJEN")
                n1 = ""


boinkies = True
while boinkies:
    print("[green]VELKOMMEN TIL GAMBLING AUTOMATEN.")
    print("[green]VIL DU (1) LEGGE INN I KONTOEN, (2) SE DEN ELLER (3)AVSLUTTE PROGRAMMET?")
    choice = ""
    while choice == "":
        print("[green]HVA VELGER DU?")
        choice = input().strip()
        if choice == "1":
            score += add()
        elif choice == "2":
            print("[green]CURRENT BALANCE IS")
            if score < 1:
                print(f"[red]{score}")
            else:
                print(f"[green]{score}")
        elif choice == "3":
            print("[green]HA DET!!!")
            boinkies = False
        else:
            print("[red]KOMANDO IKKE GJENKJENT")