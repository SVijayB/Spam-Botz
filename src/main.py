from Spammer import *
from Static import *
import time

choice = int(input("""How would you like to spam the user ? 
1) Static Message
2) Random Words From A Dictionary
3) Series of Sequential Numbers
4) Random Numbers\n>"""))

while(choice<1 or choice>4):
    print("ERROR: ENTER VALUES BETWEEN 1 AND 4 ONLY")
    choice = int(input(">"))
if(choice==1):
    message = static()

count = int(input("Enter the number of times you want to spam the message : "))
print("Open Your Social Media Platform and select your text box")
time.sleep(5)
spammer(count,message)