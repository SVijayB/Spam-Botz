import time
from Spammer import *

def static():
    message = input("Enter the String you want to spam : ")
    count = int(input("Enter the number of times you want to spam the message : "))
    print("Open Your Social Media Platform and select your text box")
    time.sleep(5)
    spammer(count,message)