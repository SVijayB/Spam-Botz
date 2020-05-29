from Modules.Spammer import *
import time

def numbers():
    try:
        count = int(input("Enter the number until which you want to spam : \n> "))
        sleep = int(input("Enter time delay(in seconds) between each message : \n> "))
    except:
        print("ERROR : Enter Only Numbers")
        input("Press any key to exit ")
        sys.exit(0)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in range(1,count+1):
        x = str(x)
        spammer(x,sleep)