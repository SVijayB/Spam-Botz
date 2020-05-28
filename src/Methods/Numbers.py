from Spammer import *
import time

def numbers():
    count = int(input("Enter the number until which you want to spam : \n> "))
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in range(1,count+1):
        x = str(x)
        spammer(x)