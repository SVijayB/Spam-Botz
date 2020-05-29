from Modules.Numbers import *
from Modules.RandNumbers import *
from Modules.Static import *
from Modules.RandomWords import *
from Modules.RageSpam import * 
import time

if __name__ == "__main__":
    data = open("../version.txt" , "r").read()
    print("Spam-Botz | " + data)
    time.sleep(1)
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