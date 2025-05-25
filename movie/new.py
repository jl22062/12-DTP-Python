import easygui

# ╔═════════════════════════════════════════════════════╗
# ║                  Dictionaries start                 ║
# ╚═════════════════════════════════════════════════════╝
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
    "admin": {"password": "admin","balance":99999999},
    "Billy": {"password": "billy", "balance": 1250.50},
    "Bobby": {"password": "bobby", "balance": 820.00},
    "Bo": {"password": "bo", "balance": 312.75},
}
# ╔═════════════════════════════════════════════════════╗
# ║                  Dictionaries end                   ║
# ╚═════════════════════════════════════════════════════╝

# ╔═════════════════════════════════════════════════════╗
# ║                   Functions start                   ║
# ╚═════════════════════════════════════════════════════╝

# Used to search for a movie by title, shows info and reviews if found, else tells you it's not real.
def searchMovie(movies):
    while True:
        title = easygui.enterbox("Enter movie title to search:", "Search Movie")
        if title is None:
            return
        title = title.strip()
        if not title:
            easygui.msgbox("Please enter a movie title.")
            continue
        for movie in movies.values():
            if title.lower() == movie["title"].lower():
                reviews = "\n".join([f'{r["name"]}: {r["comment"]}. Rating: {r["rating"]}' for r in movie["reviews"].values()])
                easygui.msgbox(f'Title: {movie["title"]}\nGenre: {movie["genre"]}\nDuration: {movie["duration"]} min\n'
                               f'Seats: {movie["seats"]}\nRating: {movie["rating"]}\n--- Reviews ---\n{reviews}', "Movie Found")
                return
        easygui.msgbox(f'The movie "{title}" does not exist.', "Not Found")

# Lets admin add a new movie to the list. Does error checks for bad input or duplicate titles.
def addMovie(movies):
    fields = ["Title", "Genre", "Duration (minutes)", "Seats Available", "Ticket Price ($)"]
    movie_details = easygui.multenterbox("Enter movie details", "Add Movie", fields)
    if movie_details is None:
        return

    title, genre, duration_str, seats_str, price_str = movie_details

    if any(not x.strip() for x in movie_details):
        easygui.msgbox("All fields are required.", "Error")
        return

    try:
        duration = int(duration_str)
        seats = int(seats_str)
        price = float(price_str)
        if duration <= 0 or seats < 0 or price <= 0:
            raise ValueError
    except ValueError:
        easygui.msgbox("Duration, seats, and price must be valid positive numbers.", "Error")
        return

    for movie in movies.values():
        if movie["title"].lower() == title.lower():
            easygui.msgbox("Movie already exists.", "Error")
            return

    new_id = str(len(movies) + 1)
    movies[new_id] = {
        "title": title,
        "genre": genre,
        "duration": duration,
        "seats": seats,
        "rating": 0,
        "reviews": {},
        "price": price
    }
    easygui.msgbox(f'Movie "{title}" added successfully with ticket price ${price:.2f}!', "Success")

# Signs a new user up. Checks if username is already taken, and if fields aren't blank.
def addUser(users):
    while True:
        info = easygui.multpasswordbox("Sign up", "Create Account", ["Username", "Password"])
        if info is None:
            return
        username, password = info[0].strip(), info[1]
        if not username or not password:
            easygui.msgbox("All fields required.", "Error")
            continue
        if username in users:
            easygui.msgbox("Username exists. Try another.", "Error")
            continue
        users[username] = {"password": password, "balance": 0.0}
        easygui.msgbox(f"User '{username}' created.", "Success")
        return

# Logs the user in. Gives 3 tries to get username and password right.
def login(users):
    for _ in range(3):
        info = easygui.multpasswordbox("Login", "Login Page", ["Username", "Password"])
        if info is None:
            return None
        username, password = info[0].strip(), info[1]
        if username in users and users[username]["password"] == password:
            easygui.msgbox(f"Logged in as {username}", "Success")
            return username
        else:
            easygui.msgbox("Incorrect login.", "Error")
    easygui.msgbox("Too many failed attempts.", "Error")
    return None

# This function is used to buy tickets, it checks ur balance and sees if you can afford it. Also checks if there’s seats left.
def buyTicket(users, movies, current_user):
    if current_user is None:
        easygui.msgbox("You must be logged in.", "Error")
        return
    movie_choices = [m["title"] for m in movies.values()]
    movie_title = easygui.choicebox("Select a movie:", "Buy Ticket", movie_choices)
    if movie_title is None:
        return
    movie_key = next((k for k, m in movies.items() if m["title"] == movie_title), None)
    if movie_key is None:
        easygui.msgbox("Movie not found.", "Error")
        return
    movie = movies[movie_key]
    if movie["seats"] <= 0:
        easygui.msgbox("No seats left.", "Sold Out")
        return
    ticket_choice = easygui.choicebox(f"{movie_title} has {movie['seats']} seats.\nHow many tickets?", "Buy", ["1", "2", "5"])
    if ticket_choice is None:
        return
    tickets = int(ticket_choice)
    if tickets > movie["seats"]:
        easygui.msgbox(f"Only {movie['seats']} seats available.", "Error")
        return
    total_cost = tickets * movie["price"]
    balance = users[current_user].get("balance", 0)
    if balance < total_cost:
        easygui.msgbox(f"Not enough balance. Need ${total_cost}, have ${balance}.", "Error")
        return
    users[current_user]["balance"] -= total_cost
    movies[movie_key]["seats"] -= tickets
    easygui.msgbox(f"Purchased {tickets} ticket(s) for {movie_title}.\nCost: ${total_cost}\nNew balance: ${users[current_user]['balance']:.2f}", "Success")

# The main menu for normal users. Lets them search for movies, buy tickets, log out, or dip.
def mainMenu(users, movies, current_user):
    while True:
        options = ["Search movie", "Buy ticket", "Logout", "Exit"]
        choice = easygui.choicebox("Main Menu", "User Options", options)
        if choice == "Search movie":
            searchMovie(movies)
        elif choice == "Buy ticket":
            buyTicket(users, movies, current_user)
        elif choice == "Logout":
            easygui.msgbox("Logged out.", "Logout")
            return None
        elif choice == "Exit" or choice is None:
            exit()

# Admin menu is just like main menu but it can also add movies. Could add more admin powers later.
def adminMenu(users, movies, current_user):
    while True:
        options = ["Add movie", "Search movie", "Buy ticket", "Logout", "Exit"]
        choice = easygui.choicebox("Admin Menu", "Admin Options", options)
        if choice == "Add movie":
            addMovie(movies)
        elif choice == "Search movie":
            searchMovie(movies)
        elif choice == "Buy ticket":
            buyTicket(users, movies, current_user)
        elif choice == "Logout":
            easygui.msgbox("Logged out.", "Logout")
            return None
        elif choice == "Exit" or choice is None:
            exit()

# This is where the whole thing starts. User can login, sign up, search movies, or just leave.
def startUp(users, movies):
    current_user = None
    while True:
        options = ["Login", "SignUp", "Search movie", "Exit"]
        choice = easygui.choicebox("Welcome! What would you like to do?", "Start Menu", options)
        # Login mode, checks your creds then sends you to the right menu.
        if choice == "Login":
            current_user = login(users)
            if current_user:
                if current_user == "admin":
                    current_user = adminMenu(users, movies, current_user)
                else:
                    current_user = mainMenu(users, movies, current_user)
        # Sign up mode if you're new.
        elif choice == "SignUp":
            addUser(users)
        # You can search for movies without logging in.
        elif choice == "Search movie":
            searchMovie(movies)
        # You can bounce anytime with Exit.
        elif choice == "Exit" or choice is None:
            exit()

# ╔═════════════════════════════════════════════════════╗
# ║                    Function ends                    ║
# ╚═════════════════════════════════════════════════════╝

# Kicks off the whole app. Passed users and movies so it doesn't rely on global vars because globel var is le bad apparently 🤡
startUp(users, movies)
