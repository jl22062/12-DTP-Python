codes = ["level", "power", "deed", "fight", "meme", "run"]
palindrome = []

for i in codes:
    if i[::-1] == i:
        palindrome.append(i)
print (palindrome)