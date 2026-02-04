from rich import print

characters = []
print("[green]WELCOME TO THE CHARACTER LIST 9000000000000000")
while True:
    print("[green]PLEASE INPUT YOUR CHARACTER (EMPTY = END)")
    char = input().strip()

    if len(char) > 50:
        print("[red]ERROR: TEXT IS LONGER THAN 50 CHARACTERS")
        char = "a buncho giberish to hopefully make iot so that nobody types this, though this seems like more than 50 so probably not worth it"
    if char in characters:
        print("[red]ERROR: ALREADY IN LIST")
        char = "a buncho giberish to hopefully make iot so that nobody types this, though this seems like more than 50 so probably not worth it"
    if char == "":
        print("[green]DONE ADDING CHARACTERS")
        print()
        break
    if not char == "a buncho giberish to hopefully make iot so that nobody types this, though this seems like more than 50 so probably not worth it":
        list.append(characters, char)
        print(f"[green]CHARACTER \\[{char}] ADDED SUCCESSFULLY")
    print()

print("[green]PRINTING THEM OUT NOW")
print()
if len(characters) == 0:
    print("[red]YOU DIDN'T EVEN ADD ANY? NOW I WILL LAUGH AT YOU FOREVER")
    input()
    while True:
        print("[red]HAHAHAHAHAHAHA")
for i in range(len(characters)):
    print(f"[green]{i+1}) {characters[i]}")