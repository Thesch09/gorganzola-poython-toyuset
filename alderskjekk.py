navn_paa_butique = ["FUGLER", "OIXEAUS", "MAT", "MATTE", "PYTHON", "HOPES", "AND", "DREAMS", "den døde", "UNDERTALE", "LIBRARBY", "sans'", "GAY"]
import random
from playsound3 import playsound
import time

sfx = playsound


butique_navn = random.randint(0, len(navn_paa_butique)-1)

navn = navn_paa_butique[butique_navn].split()
if navn[len(navn)-1] == "S":
    navn.remove(navn[len(navn)-1])

nyNavn = ""
for i in range(len(navn)):
    nyNavn += navn[i]

print(f"VELKOMMEN TIL PROFESSOR {nyNavn}S KARAKTER KALKULATOR")
print(f"FØRST OG FREMST, HVOR GAMMEL ER DU")

alder = ""
bro = True
while True:
    while alder == "":
        try:
            alder = input().strip()
            alder = int(alder)
        except ValueError:
            print(f"BZZT! {alder} ER IKKE ET HELTALL! JEG TRENGER ET HELTALL")
            alder = ""
    if alder >= 18:
        print(f"FOLK SOM ER {alder} ER FOR GAMLE FOR... vent et sekund det høres feil ut...")
        print(f"DU ER LITT FOR GAMMEL FOR DET JEG GJØR!")
        bro = False
        break
    elif alder < 13:
        print(f"SIDEN DU ER {alder} ÅR GAMMEL, ER DU FOR UNG! HAHA")
        bro = False
        break
    else:
        break

if bro:
    print(f"NÅ HVOR MANGE POENG HAR DU? MELLOM 0 OG 100 SELVFØLGELIG")
    poeng = ""
    while poeng == "":
        try:
            poeng = input().strip()
            poeng = int(poeng)
            if poeng > 100:
                print(f"BZZT! {poeng} ER MER ENN 100!")
                poeng = ""
            elif poeng < 0:
                print(f"BZZT! {poeng} ER MINDRE ENN 0!")
                poeng = ""
        except ValueError:
            print(f"BZZT! {poeng} ER IKKE ET HELTALL! JEG TRENGER ET HELTALL")
            poeng = ""

    if poeng < 35:
        print("OO. DU FIKK BARE EN ENER...")
    elif poeng <= 50:
        print("DU FIKK EN TOER. DET ER I HVERTFALL BEDRE ENN EN ENER.")
    elif poeng <= 65:
        print("DU FIKK EN TREER. DET ER IKKE EN DÅRLIG KARAKTER.")
    elif poeng <= 80:
        print("DU FIKK EN FIRER. BRA FOR DEG")
    elif poeng <= 90:
        print("DU FIKK EN FEMER. DET ER VELDIG BRA")
    else:
        print("DU FIKK EN SEKSER! DET ER EKSTREMT BRA! DU SKAL VÆRE GLAD. NÅ!")
        