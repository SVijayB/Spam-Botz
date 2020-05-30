import time
from Modules.Spammer import *

def static():
    message = input("Enter the String you want to spam : \n> ")
    try:
        count = int(input("Enter the number of times you want to spam the message : \n> "))
        sleep = float(input("Enter time delay(in seconds) between each message : \n> "))
    except:
        print("ERROR : Enter Only Numbers")
        input("Press any key to exit ")
        sys.exit(0)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for i in range(count):
        spammer(message,sleep)