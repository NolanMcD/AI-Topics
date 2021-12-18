import random
import time

xpay = (20 * (1/64)) + (15 * (1/64)) + (5 * (1/64)) + (3 * (1/64)) + (2 + (1/16)) + (1 * (1/4))
print("Expected payback " + str(xpay))
print("Prob that 1 coin will result in a win is " + str(19/64))
machine = ["BAR","BELL","LEMON","CHERRY"]
coins = 10
plays = 0
while coins > 0:
    plays += 1
    randy1 = random.randint(0,3)
    randy2 = random.randint(0,3)
    randy3 = random.randint(0,3)
    spin = [machine[randy1],machine[randy2],machine[randy3]]
    cherrycount = 0
    for x in spin:
        if x == "CHERRY":
            cherrycount += 1
    if spin == ["BAR","BAR","BAR"]:
        coins += 20
    elif spin == ["BELL","BELL","BELL"]:
        coins += 15
    elif spin == ["LEMON","LEMON","LEMON"]:
        coins += 5
    elif spin == ["CHERRY","CHERRY","CHERRY"]:
        coins += 3
    elif spin[0] == "CHERRY" and spin[1] == "CHERRY":
        coins += 2
    elif spin[0] == "CHERRY":
        coins += 1
    coins -= 1
    print("spin was" + str(spin))
    #time.sleep(.5)
    print("coins is: " + str(coins))

print("Plays: " + str(plays))
