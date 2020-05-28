from Spammer import *
from Static import *
import time

try:
    choice = int(input("""How would you like to spam the user ? 
    1) Static Message
    2) Random Words From A Dictionary
    3) Series of Sequential Numbers
    4) Random Numbers"""))
    if(choice!=1 or choice!=2 or choice!=3 or choice!=4):
        raise ValueError
except ValueError:
    print("Select Values Between 1-4 only")
if(choice==1):
    message = static()

count = int(input("Enter the number of times you want to spam the message : "))
print("Open Your Social Media Platform and select your text box")
time.sleep(5)
spammer(count,message)