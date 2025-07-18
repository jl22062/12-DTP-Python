import easygui
movies = {
    "1": {
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
    "2": {
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
    "3": {
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

def searchMovie(title):
    for movie_number in movies:
        if title.lower() != movies[movie_number]["title"].lower():
            print("not a thing")
        else:
            movie = title
            genre = movies[movie_number]["genre"]
            duration = movies[movie_number]["duration"]
            seats = movies[movie_number]["seats"]
            rating = movies[movie_number]["rating"]

            for review_number in movies[movie_number]["reviews"]:
                reviews_name = movies[movie_number]["reviews"][review_number]["name"]
                review_rating = movies[movie_number]["reviews"][review_number]["rating"]
                review_comment = movies[movie_number]["reviews"][review_number]["comment"]
            print(f'Found results for "{title}"')
            print(f"{movie}\n{genre}\n{duration}\n{seats}\n{rating}\n---\nReviews\n---\n{reviews_name}: {review_comment}. Rating: {review_rating}")
            #add easy gui


def addmovie(title,genre,duration,seats):
    for i in movies:
        titles = movies[i]["title"]
    if title == titles:
        print("Movie is already in the libiary")
    else:
        movies[len(movies)+1] = {"title": title, "genre": genre, "duration": duration,"seats": seats}

def addUser():
        x = [
        "username",
        "password",
        ]
        msg = "Sign up"
        title = "Sign up page"
        
        loginPage = easygui.multpasswordbox(msg,title,x)
        for i in range(len(x)):
            while x[i].strip() == "":
                error = "Please fill the boxes"
                loginPage = easygui.multpasswordbox(error,title,x)
        username = loginPage[0]
        password = loginPage[1]
        users[username] = {"password":password, "balance":"0"}  #flexable efficient, robust
        print(users)
        startUp()

def login():
        x = [
        "username",
        "password",
        ]
        msg = "Login"
        title = "Login page"
        
        loginPage = easygui.multpasswordbox(msg,title,x)
        for i in range(len(x)):
            while x[i].strip() == "":
                error = "Please fill the boxes"
                loginPage = easygui.multpasswordbox(error,title,x)
        username = loginPage[0]
        password = loginPage[1]
        return username, password
def function(x):
    if x == "1":
        UNP = login()
        print(UNP[1])
        username = UNP[0]
        def checkPasswords():
            if UNP[1] == users[username]["password"]:
                print(f"Logged in as {username}")
                startUp()
            else:
                print("Incorrect password")
                function(1)
        if username == "admin":
            if UNP[1] == "admin":
                print("Signed in as admin")
                adminPerms = True
                startUp()
            else:
                print("Wrong password try again.")
                function(1)
        elif username in users:
            print("Valid user")
            checkPasswords()
        else:
            print("Invalid user")
            function("1")
    elif x == "2":
        addUser()
    elif x == "3":
        title = input("Movie title: ")
        searchMovie(title)

def startUp():
    adminPerms = False
    if adminPerms is False:
        functionType = input("Start menu\n1. Login\n2. Signup\n3. Search movies\nSelect a function: ")
        function(functionType)

startUp()