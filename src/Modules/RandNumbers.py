import random
from Modules.Spammer import *
import time
import sys

def randomnum():
    print("\n-----LARGE NUMBERS SPAM-----")
    print("This spamming method spams random numbers from 1 - 999999999 each as a seperate message\n")
    try:
        count = int(input("Enter the number of spam messages you want to send \n> "))
        sleep = float(input("Enter time delay(in seconds) between each message \n> "))
    except:
        print("ERROR : Enter Only Numbers")
        input("Press any key to exit ")
        sys.exit(0)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(5)
    for x in range(count):
        num = random.randint(1,999999999)
        term = str(num)
        spammer(term,sleep)