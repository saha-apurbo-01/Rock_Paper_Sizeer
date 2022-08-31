import random
def gameWin(com,you):

    if comp == you:
        return None
    elif comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False
    elif comp == "p":
        if you == "r":
            return False
        elif you == "s":
            return True
    elif comp == "s":
        if you == "p":
            return False
        elif you == "r":
            return True
comp = input("computer turn: Rock(r) Paper(p) Sizer(s) :")
ranNo = random.randint(1,3)
if ranNo == 1:
    comp = "r"
elif ranNo == 2:
    comp = "p"

elif ranNo == 3:
    comp = "s"

you = input("your  turn: Rock(r) paper(p) sizer(s) :")
comp = gameWin(comp,you)
print("computer choose :")
print(ranNo)
print("you choose :")
print(f"{you}")
if comp == None:
    print("the game is tie! Play again!!!")
elif comp:
    print("you win")
else:
    print("you lose")
