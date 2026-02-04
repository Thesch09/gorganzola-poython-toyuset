navn_paa_butique = ["FUGLER", "OIXEAUS", "MAT", "MATTE", "PYTHON", "HOPES", "AND", "DREAMS", "den døde", "UNDERTALE", "LIBRARBY", "sans'"]
import random
from playsound3 import playsound
import time

sfx = playsound


butique_navn = random.randint(0, len(navn_paa_butique)-1)

print(f"VELKOMMEN TIL {navn_paa_butique[butique_navn]} BUTIKKEN!")
print("HVA VIL DU KJØPE?")

ting = input().strip()

print(f"OK! HVOR MYE KOSTER {ting}?")

while True:
    try:
        pris = input().strip()
        pris = float(pris)
        break
    except ValueError:
        print(f"BZZT! {pris} ER IKKE ET DESIMALTALL! JEG TRENGER ET DESIMALTALL")

print(f"OK! HVOR MANGE {ting} VIL DU KJØPE?")
while True:
    try:
        maur = input().strip()
        maur = int(maur)
        break
    except ValueError:
        print(f"BZZT! {maur} ER IKKE ET HELTALL! JEG TRENGER ET HELTALL")

input("TRYKK [ENTER] FOR Å FORTSETTE \n")

totpris = pris * maur
print(f"{maur} {ting} KOSTER {totpris}")

print(f"HER PÅ {navn_paa_butique[butique_navn]} BUTIKKEN HAR VI DELIVERY!")
print(f"OM HVOR MANGE SEKUNDER VIL DU HA INNKJØPET DITT?")

while True:
    try:
        sec  = input().strip()
        sec = float(sec)
        break
    except ValueError:
        print(f"BZZT! {sec} ER IKKE ET DESIMALTALL! JEG TRENGER ET DESIMALTALL")

input("TRYKK [ENTER] FOR Å FORTSETTE \n")
mins = 0
temp = sec
while temp >= 60:
    mins += 1
    temp -= 60

print(f"OK! PAKKEN DIN KOMMER OM {mins} MINUTTER OG {temp} SEKUNDER!")

time.sleep(sec)
sfx("goofs/car-crash_OwBDipR.mp3")
print("TAKK FOR AT DU KJØPTE OSS HOS!")