from Methods.Numbers import *
from Methods.RandNumbers import *
from Methods.Static import *
from Methods.RandomWords import *
from Methods.RageSpam import * 

if __name__ == "__main__":
    print("Spam-Botz | v1.0.0")
    time.sleep(0.5)
    choice = int(input("""How would you like to spam ? 
    1) Static Message
    2) Random Words From A Dictionary
    3) Series of Sequential Numbers
    4) Random Numbers
    5) Rage Spam\n> """))

    while(choice<1 or choice>5):
        print("ERROR: ENTER VALUES BETWEEN 1 AND 5 ONLY")
        choice = int(input("> "))
    if(choice==1):
        static()
    if(choice==2):
        randwords()
    if(choice==3):
        numbers()
    if(choice==4):
        randomnum()
    if(choice==5):
        rage()