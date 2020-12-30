import random
# import time
a = ["s", "w", "g"]
name = input("Enter your name:\n")
scoreman = 0
scorecomp = 0
total_chance = 10
no_of_chance = 0
print("You have to enter s for snake, w for water and g for gun.")
while no_of_chance < total_chance:
    _chance = input("Enter: (s, g, w)\n") 
    _comp_chance = random.choice(a)
    # time.sleep(2)
    print("Computer:", _comp_chance)
    if _chance == "s" and _comp_chance == "w":
        scoreman = scoreman+1
        print("You won")
    elif _chance == "s" and _comp_chance == "g":
        scorecomp = scorecomp + 1
        print("computer won")
    elif _chance == "w" and _comp_chance == "s":
        scorecomp = scorecomp+1
        print("computer won")
    elif _chance == "w" and _comp_chance == "g":
        scoreman = scoreman + 1
        print("you won")
    elif _chance == "g" and _comp_chance == "w":
        scorecomp = scorecomp+1
        print("computer won")
    elif _chance == "g" and _comp_chance == "s":
        scoreman = scoreman + 1
        print("you won")
    elif _chance == "g" and _comp_chance == "g":
        print("its a tie")
    elif _chance == "s" and _comp_chance == "s":
        print("its a tie")
    elif _chance == "w" and _comp_chance == "w":
        print("its a tie")
        # pass 
    else:
        print("Invalid Input.")
    no_of_chance += 1
    
if scorecomp > scoreman:
    print("Computer won at all.")
    print("better luck next time")
    print("Computer's score:",scorecomp)
    print("Your score:", scoreman)
elif scorecomp < scoreman:
    print("You won at all")
    print("Computer's score:",scorecomp)
    print("Your score:", scoreman)
else:
    print("Its a tie at all")
    print("Computer's score:",scorecomp)
    print("Your score:", scoreman)
