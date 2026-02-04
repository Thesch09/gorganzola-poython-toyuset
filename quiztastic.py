from rich import print
import random

class Question:
    def __init__(self, question, correct, cor_id, ans_a, ans_b, ans_c="", ans_d=""):
        self.question = question
        self.correct = correct
        self.cor_id = cor_id
        self.ans_a = ans_a
        self.ans_b = ans_b
        self.ans_c = ans_c
        self.ans_d = ans_d





sansQuest = Question("Who is sans?", "c", "Papyrus' brother", "Ness", "The Skeleton", "Papyrus' brother", "Spamton")
kaleSonic = Question("Which one of these is not voiced by the same guy as Kale Vandelay", "b", "Sonic (2020)", "Sonic", "Sonic (2020)", "Sonic", "Sonic")
silksongDate = Question("When was Silksong released?", "d", "04.09.2025", "04.06.2025", "04.04.2004", "24.02.2017", "04.09.2025")
programming = Question("I don't like programming.", "b", "False", "True", "False", "", "")

questions = [sansQuest, kaleSonic, silksongDate, programming]


score = 0

def ask_question(question, pointsies):
    ans = ""
    possible_ans = ["a", "b", "c", "d"]
    print(f"[green]{question.question}")
    input()

    print(f"[dark_goldenrod]A) {question.ans_a}")
    print(f"[blue]B) {question.ans_b}")
    if question.ans_c == "":
        list.remove(possible_ans, "c")
    else:
        print(f"[yellow]C) {question.ans_c}")
    if question.ans_d == "":
        list.remove(possible_ans, "d")
    else:
        print(f"[purple]D) {question.ans_d}")

    input()
    print("[green]What do you pick?")
    while not ans in possible_ans:
        ans = input().lower().strip()
        if not ans in possible_ans:
            print("[red]That's not an option.")

        
    print(f"[green]And the correct answer is?")
    temp1 = question.cor_id
    print(f"[green]{question.cor_id}!")
    if ans == question.correct:
        print("[green]Which means you got that question correct!")
        print(f"[green]You get {pointsies} points!")
        return(pointsies)
        
    else:
        print("[red]Which means you're WRONG-A-MUNDO!")
        print(f"[red]You lose {pointsies*2} points!")
        return(pointsies*-2)

print("[green]Welcome to the Quiztastic Quiz")
while True:
    rand = random.randint(0, len(questions)-1)
    score += ask_question(rand, 5)
    print(f"[green]You currently have {score} points!")
    print()
    print("[green]New question time!")