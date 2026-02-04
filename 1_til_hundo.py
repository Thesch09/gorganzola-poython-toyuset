items = ["a python guide", "a pardrigde in a pear tree", "PERSONA 6 POGIES!!!", "a burger", "a divorce", "a wedding ring", "a motivational speech clearly written by AI, so I broke up with them", "pain", "french bread", "a word pronounced \"wazo\"", "SILKSONG!!!", "a coma", "Hi-Fi Rush!", "Luigi", "a child. Like this isn't my child, they just gave me a random.randint child of the streets. Like why???????"]

import random

for i in range(100):
    print(f"On day number {i+1} of the apocalypse my true love gave to me {items[random.randint(0, len(items)-1)]}")

print("GOD IF YOU GIVE ME SOME NUMBERS AND I SAY THE SUM, WILL YOU PLEASE END THIS APOCALYPSE, PLEASE?")

numbahs = []


times = ""
while times == "":
    try:
        times = input("HOW MANY NUMBERS??? ").strip()
        times = int(times)
    except ValueError:
            print(f"PLEASE JUST MAKE {times} A WHOLE NUMBER PLEASE")
            times = ""

for i in range(times):
    num1 = ""
    while num1 == "":
        try:
            num1 = input("Please give us a chance...").strip()
            num1 = int(num1)
        except ValueError:
                print(f"{num1} isn't a whole number, just give us a chance")
                num1 = ""

    list.append(numbahs, num1)


print(f"Well God, the sum is {sum(numbahs)}")


damnation = input("Type no if you want them to suffer for eternity >:)").lower().strip()
if damnation == "no":
    print("WHY HAVE YOU PUNISHED US YET AGAIN!!! AUASHDHUIOAGODF!!!!")