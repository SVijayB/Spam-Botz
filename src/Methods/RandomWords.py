import urllib.request
import random
from Spammer import *
import time

def randwords():
    url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(url)
    data = str(response.read().decode())
    words = data.splitlines()
    count = int(input("Enter the number of words you want to spam : \n> "))
    randwords = random.sample(words,count)
    print("Open Your Social Media Platform and select your text box. Wait for atleast 15 seconds")
    time.sleep(15)
    for x in randwords:
        spammer(x)