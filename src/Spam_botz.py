from Modules.Numbers import *
from Modules.RandNumbers import *
from Modules.Static import *
from Modules.RandomWords import *
from Modules.RageSpam import * 
from Modules.SentenceBreaker import *
import time

if __name__ == "__main__":
    logo = open("../assets/logo.txt","r")
    output = "".join(logo.readlines())
    print(output)
    print("\n"+"-"*20)
    data = open("../assets/version.txt" , "r").read()
    print("Spam-Botz | " + data)
    time.sleep(1)
    while(True):
        print("""What would you like to do ? 
        1) Static Message Spam
        2) Spam Random Words From A Dictionary
        3) Spam A Series of Sequential Numbers
        4) Spam Random Large Numbers
        5) Sentence breaker(into words) Spam
        6) Rage Spam
        7) EXIT""")
        choice = 0
        while(choice<1 or choice>7):
            try:
                choice = int(input("> "))
                if(choice<1 or choice>7):
                    raise ValueError
            except ValueError:
                print("ERROR : INVALID NUMBER")
        if(choice==1):
            static()
        if(choice==2):
            x = open("../assets/dictionary.txt","r")
            data = x.read()
            randwords(data)
            x.close()
        if(choice==3):
            numbers()
        if(choice==4):
            randomnum()
        if(choice==5):
            sentencebreaker()
        if(choice==6):
            rage()
        if(choice==7):
            print("-----x Thank You For Using Spam-Botz x-----")
            input("Press any key to exit ")
            break
        print("\nSuccessfully Completed Spamming")
        ans = input("Do you want to continue your adventure on spamming? (Yes/No)\n> ")
        if(ans=="Yes" or ans=="yes" or ans=="y" or ans=="Y"):
            print("\nJourney Continues...\n")
        elif(ans=="no" or ans=="No" or ans=="N" or ans=="n"):
            print("-----x Thank You For Using Spam-Botz x-----")
            input("Press any key to exit ")
            break
        else:
            print("ERROR : INVALID INPUT")
            input("Press any key to exit ")
            break