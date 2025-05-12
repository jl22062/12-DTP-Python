movies = {
    "M001": {
        "title": "Inception",
        "genre": "Sci-Fi",
        "duration": 148,
        "seats": 85,
        "rating": 6,
        "reviews": {
            1: {"name": "Adam", "rating": 6, "comment": "Amazing plot!"},
        },
        "price": 12,
    },
    "M002": {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "duration": 169,
        "seats": 110,
        "rating": 4.6,
        "reviews": {
            1: {"name": "Jane", "rating": 4.6, "comment": "Mind-expanding!"},
        },
        "price": 13,
    },
    "M003": {
        "title": "Joker",
        "genre": "Drama",
        "duration": 122,
        "seats": 100,
        "rating": 8.0,
        "reviews": {
            1: {"name": "Jason", "rating": 8.0, "comment": "Dark and intense."},
        },
        "price": 12,
    },
}
 
users = {
    "admin": {"password": "admin"},
    "Billy": {"password": "billy", "balance": 1250.50},
    "Bobby": {"password": "bobby", "balance": 820.00},
    "Bo": {"password": "bo", "balance": 312.75},
}

def checkPasswords():
        pw = input("Please enter your password: ")
        if pw == users[username]["password"]:
            print(f"Logged in as {username}")
            global loginState
            loginState = True
        else:
            print("Incorrect password")
            checkPasswords()

def attemptLogin():
    if username == "admin":
        print("Attempting to sign in as admin")
    elif username in users:
        print("Valid user")
        checkPasswords()
    else:
        print("Invalid user")
        attemptLogin()

def searchMovie(x):
    if loginState == True:
        input("Please enter movie name ")
    else:
        print("Log in first")

username = input('Username: ')
attemptLogin()
searchMovie()

