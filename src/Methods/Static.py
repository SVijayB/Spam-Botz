import time
from Spammer import *

def static():
    message = input("Enter the String you want to spam : \n> ")
    count = int(input("Enter the number of times you want to spam the message : \n> "))
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for i in range(count):
        spammer(message)