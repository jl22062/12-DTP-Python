import time as t

def quiz():
    #Questions
    question = input("Water bucket, _______\n")
    if question.lower() == 'release':
        print("Correct!")
        t.sleep(0.5)
        question2 = input("I... AM, _____\n")
        if question2.lower() == 'steve':
            print("Correct!")
            t.sleep(0.5)
            question3 = input("CHICKEN ______\n")
            if question3.lower() == 'jockey':
                print("You got all 3 questions correct, congrats!")
            else:
                print("Incorrect")
                quiz()
        else:
            print("Incorrect")
            quiz()
    else:
        print("Incorrect")
        quiz()

#Stupid thingy
print("I'm gonna ask you 3 questions, if you fail you have to restart.")
t.sleep(1)
print("Ready?")
t.sleep(1)
print("3")
t.sleep(1)
print("2")
t.sleep(1)
print("1")
t.sleep(1)
print("Begin")
t.sleep(1)
quiz()