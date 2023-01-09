
def reply(use):
    replyp = ["yes","yep","yeah","sure","yup","of course"]
    replyn = ["no","nah","nope",]
    for rep in replyp:
        rep = rep.capitalize()
        if rep == use:
            print("\n")
    for repn in replyn:
        repn = repn.capitalize()
        if repn == use:
            print("Bye")
            quit()
            
def remain():
    global life
    life = 100
    print(f"You have a {life} percent life")
    
