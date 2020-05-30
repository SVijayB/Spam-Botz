import urllib.request
import random
from Modules.Spammer import *
import time

def randwords():
    print("\n-----RANDOM DICTIONARY WORDS SPAM-----")
    print("This spamming method spams random dictionary words\n")
    url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(url)
    data = str(response.read().decode())
    words = data.splitlines()
    try:
        count = int(input("Enter the number of words you want to spam \n> "))
        sleep = float(input("Enter time delay(in seconds) between each message \n> "))
    except:
        print("ERROR : Enter Only Numbers")
        input("Press any key to exit ")
        sys.exit(0)
    randwords = random.sample(words,count)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in randwords:
        spammer(x,sleep)