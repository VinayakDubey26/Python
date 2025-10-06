import random

def gameWin(comp,user):
    if user==comp:
        return "It's a Tie"
    elif (user=="rock" and comp=="scissor") or (user=="scissor" and comp=="paper") or (user=="paper" and comp=="rock"):
        return "You Win"
    else:
        return "You Lose"
    
choices = ["rock","paper","scissor"]

print("Choose: Rock(r) Paper(p) Scissor(s)?")
user_input = input("Enter your choice: ").lower()

if user_input not in ['r','p','s']:
    print("Invalid input! Please choose rock, paper, or scissor.")
else:
    comp_input = random.choice(choices)
    print(f"Computer chose: {comp_input}")

    result = gameWin(comp_input,user_input)
    print(result)