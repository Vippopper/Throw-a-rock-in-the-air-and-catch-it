import random
import time
count = 0
debug = 0
print("You have a rock. Type throw to throw it in the air. Type catch to catch it.")
while True:
    while True:
        throw = input()
        if throw.casefold() == "throw":
            print("You threw the rock.")
            ttime1 = time.time()
            break
        if throw == "seecatchtime":
            debug = 1
            print("seecatchtime mode on")
    while True:
        catch = input()
        if catch.casefold() == "catch":
            ttime2 = time.time()
            if debug == 1:
                print(ttime2 - ttime1)
            break
    if ttime2 - ttime1 > 1.5 and ttime2 - ttime1 < 2:
        print("You caught the rock.")
        count += 1
    else:
        print(f"You did not catch the rock.\nYou caught the rock {count} times before you missed.")
        count = 0