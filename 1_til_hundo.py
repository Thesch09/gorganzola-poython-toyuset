items = ["a python guide", "a pardrigde in a pear tree", "PERSONA 6 POGIES!!!", "a burger", "a divorce", "a wedding ring", "a motivational speech clearly written by AI, so I broke up with them", "pain", "french bread", "a word pronounced \"wazo\"", "SILKSONG!!!", "a coma", "Hi-Fi Rush!", "Luigi", "a child. Like this isn't my child, they just gave me a random.randint child of the streets. Like why???????"]

import random

for i in range(100):
    print(f"On day number {i+1} of the apocalypse my true love gave to me {items[random.randint(0, len(items)-1)]}")

print("GOD IF YOU GIVE ME 2 NUMBERS AND I SAY WHICH ONE IS THE LARGER ONE, WILL YOU PLEASE END THIS APOCALYPSE, PLEASE?")

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

damnation = input("Type no if you want them to suffer for eternity >:)").lower().strip()
if damnation == "no":
    print("WHY HAVE YOU PUNISHED US YET AGAIN!!! AUASHDHUIOAGODF!!!!")