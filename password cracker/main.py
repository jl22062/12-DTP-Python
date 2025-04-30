import time as t
status = False
tries = 0

while status == False:
    password = "urboos"
    enteredPassword = input("Please enter your password...\n")
    if enteredPassword == "urboos":
        status = True
    else:
        print("Incorrect password, try again.")
        tries = tries+1
        if tries > 4:
            print("Too much incorrect attempts. Enjoy the 5 minute cooldown :D")
            t.sleep(60*5)