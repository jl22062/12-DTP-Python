import random

line_number = random.randint(1,851)
file = open("Hangman/texts.txt", "r")
for current_line_number, line in enumerate(file, start=1):
    if current_line_number == line_number:
        word = line.strip()
        attempts = int(len(word)) + 5
        print(word)
        print("_" * len(word), "the word is ", len(word), "long, you have ", attempts, "attempts.") 



