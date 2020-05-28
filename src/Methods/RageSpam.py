import random
import string
import time
from Spammer import *

def message():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    num = random.randint(5,10)
    spam = ""
    for x in range(num):
        spam = spam + "".join(random.choice(chars))
    return(spam)

def rage():
    try:
        count = int(input("Enter the number of spam messages you want to send : \n> "))
        sleep = int(input("Enter time delay(in seconds) between each message : \n> "))
    except:
        print("ERROR : Enter Only Numbers")
        input("Press any key to exit ")
        sys.exit(0)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in range(count):
        msg = message()
        spammer(msg,sleep)