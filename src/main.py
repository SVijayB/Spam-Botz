from Static import *
from RandomWords import *

if __name__ == "__main__":
    choice = int(input("""How would you like to spam the user ? 
    1) Static Message
    2) Random Words From A Dictionary
    3) Series of Sequential Numbers
    4) Random Numbers\n> """))

    while(choice<1 or choice>4):
        print("ERROR: ENTER VALUES BETWEEN 1 AND 4 ONLY")
        choice = int(input("> "))
    if(choice==1):
        static()
    if(choice==2):
        randwords()
    if(choice==3):
        numbers()
    if(choice==4):
        randomnum()