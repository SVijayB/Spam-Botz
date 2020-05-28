from Methods.Numbers import *
from Methods.RandNumbers import *
from Methods.Static import *
from Methods.RandomWords import *
from Methods.RageSpam import * 

if __name__ == "__main__":
    print("Spam-Botz | v1.0.0")
    time.sleep(0.5)
    print("""How would you like to spam ? 
    1) Static Message
    2) Random Words From A Dictionary
    3) Series of Sequential Numbers
    4) Random Numbers
    5) Rage Spam""")
    choice = 0
    while(choice<1 or choice>5):
        try:
            choice = int(input("> "))
            if(choice<1 or choice>5):
                raise ValueError
        except ValueError:
            print("ERROR : INVALID NUMBER")
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