import random           # module choose random numbers

def game(comp,you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you =='s':
            return False
    elif comp == 'p':
        if you == 'r':
            return False
        elif you =='s':
            return True
    elif comp == 's':
        if you == 'r':
            return True
        elif you =='p':
            return False
    
print("ComputerTurn: Rock(r) Paper(p) Scissor(s)")
RandomNo = random.randint(1,3)
# print(RandomNo)
if RandomNo == 1:
    comp = 'r'
elif RandomNo == 2:
    comp = 'p'
elif RandomNo == 3:
    comp = 's'

you = input("YourTurn: Rock(r) Paper(p) Scissor(s): ")
a = game(comp,you)

print("Computer Choose:", comp )
print("You Choose:", you )

if a == None:
    print("Tie")
elif a:
    print("Win")
else:
    print("Loose")



