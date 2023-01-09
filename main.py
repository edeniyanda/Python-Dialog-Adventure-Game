
from cgi import print_form
import func

print("Good day!")
name = input("What is your name? ").capitalize()
while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        break
    except:
        print("Invalid input\nPlease Enter a numeric data")
        continue
if (age >= 15) and (age < 80):
    print(f"Hey {name}, your are old enough to play\n")
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
  
    


print(">>>...Welcome to IO\n\n\n\nYou explore the jungle with 100 percent life\n\n\nYou'll be given an assistance, who will be of guide to you!")
assistance = "Eden"
print(f"\n\n>>>By default your assistance name is {assistance}\n\n")
c_n = input("Do you like to change your assistance's name?\n")

while True:
    print("\n")
    try:
        c_n = str(c_n)
        replyp = ["yes","yep","yeah","sure","yup","of course"]
        replyn = ["no","nah","nope",]
        for word in replyn:
            if c_n == word:
                print(f"Alright!!! Your assistance's name is {assistance}\n\n")   
        for word in replyp:
            if c_n == word:
                assistance = input("Enter your assistance's new name: \n")
                print(f"Your assistance name has been change from Eden to {assistance}\n\n")
        break
            
            
    except:
        print("Invalid input, please answer with a 'yes' or 'no' ")
        continue


print(f">>{assistance}: Hey {name}, I'll be your JARVIS in through out your adventure in IO \n")
input("You:\n\n")

print("Well, well, well!!\nI'm not that intelligent to understand what you said\nAll i know is that the adventure has began!!")

dir = input(f"{assistance}: Your choice, North, South, East, West!! ").lower()

def North():
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



