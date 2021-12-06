# Coded By Daniyal Arteshdar(Py.Dan)
import random

num = random.randint(0, 100)
RG = 7

while True:
    print()
    print("........................................\n")
    print("!!Hello,Guess the number !!\n")
    print(" Remaining chances : ", RG)
    gsn = float(input("* please guess number between (1, 100) : "))
    print()
    try:
        if num > gsn:
            if abs(num - gsn) < 10 :
                 print("!! It's LOW but near !!")
            elif  abs(num - gsn) > 10 :
                print("!! It's too LOW !!")

        elif num < gsn:
            if abs(num - gsn) < 10 :
                 print("!! It's HIGH but near !!")
            elif  abs(num - gsn) > 10 :
                print("!! It's too HIGH!!")

        else:
            print("** YOU WIN **")
            break

        RG = RG - 1
        if RG == 0:
            print("!! YOU LOSE !!")
            print("?? the number was ", num)
            break
    except:
        gsn = 101110010
    if gsn == 101110010:
        print("The entered input is not a number")
    else:
        print("Guess again... .  .   .")
