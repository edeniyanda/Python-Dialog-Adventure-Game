from time import sleep
from cgi import print_form
import func

print("Good day!")
sleep(1)
name = input("What is your name? ").capitalize()

while True:
    sleep(0.5)
    age = input("How old are you? ")
    try:
        age = int(age)
        break
    except:
        sleep(0.5)
        print("Invalid input\nPlease Enter a numeric data")
        continue
if (age >= 15) and (age < 80):
    sleep(0.5)
    print(f"Hey {name}, your are old enough to play\n")
    sleep(1)
elif age < 15 :
    wait = 15 - age
    s = "s"
    if wait == 1:
        s = ""
    print(f"{name}, please wait for {wait} year{s} more to play")
    quit()
else:
    print(f"{name}, your damn too old")
    quit()
start = input("You wanna play? ").capitalize()

 
func.reply(start)    
  
    


print(">>>...Welcome to IO\n\n\n\n")
sleep(1)
print(">>>You explore the jungle with 100 percent life\n\n\n")
sleep(1)
print("You'll be given an assistance, who will be of guide to you!")
assistance = "Eden"
sleep(2)
print(f"\n\n>>>By default your assistance name is {assistance}\n\n")
sleep(1)
c_n = input("Do you like to change your assistance's name?\n")

while True:
    print("\n")
    try:
        c_n = str(c_n)
        c_n.lower()
        replyp = ["yes","yep","yeah","sure","yup","of course","y","n"]
        replyn = ["no","nah","nope",]
        for word in replyn:
            if c_n == word:
                sleep(1)
                print(f"Alright!!! Your assistance's name is {assistance}\n\n")  
                sleep(1) 
        for word in replyp:
            if c_n == word:
                assistance = input("Enter your assistance's new name: \n")
                sleep(0.5)
                print(f"Your assistance name has been change from Eden to {assistance}\n\n")
                sleep(1)
        break
            
            
    except:
        sleep(1)
        print("Invalid input, please answer with a 'yes' or 'no' ")
        continue


print(f">>{assistance}: Hey {name}, I'll be your JARVIS in through out your adventure in IO \n")
sleep(2)
input("You:")
sleep(1)
print("Well, well, well!!\nThe adventure into IO has began!!")
sleep(2)
dir = input(f"{assistance}: Your choice, North, South, East, West!! ").lower()

def North():
    sleep(1)
    print(f"{assistance}: Good choice {name}\n\nWOuld you like to walk or run? ")
    action1 = input("\nYou:")
    
    if action1 == "run":
        print("You are in problem")

    print(f"\n{assistance}: Would you like to walk or run again? ")
    action2 = input("\nYou:")
    
    if action2 == "run":
        print("Your Safe")
        
    action3 = input("\nYou:")
    if action3 == "run":
        print("Your Safe")
    
    else:
        print("You are in problem")
        
if dir == "north":
    North()



