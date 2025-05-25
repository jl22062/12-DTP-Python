import easygui

# List all the current movies as a dictionary
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

# List all the current users as a dictionary
users = {
    "admin": {"password": "admin"},
    "Billy": {"password": "billy", "balance": 1250.50},
    "Bobby": {"password": "bobby", "balance": 820.00},
    "Bo": {"password": "bo", "balance": 312.75},
}

current_user = None

def searchMovie():
    while True:
        title = easygui.enterbox("Enter movie title to search:", "Search Movie")
        if title is None:
            return
        title = title.strip()
        if not title:
            easygui.msgbox("Please enter a movie title.")
            continue
        found = False
        for movie_number, movie_data in movies.items():
            if title.lower() == movie_data["title"].lower():
                found = True
                reviews_text = ""
                for rev_num, review in movie_data["reviews"].items():
                    reviews_text += f'{review["name"]}: {review["comment"]}. Rating: {review["rating"]}\n'
                easygui.msgbox(
                    f'Found results for "{title}":\n'
                    f'Title: {movie_data["title"]}\n'
                    f'Genre: {movie_data["genre"]}\n'
                    f'Duration: {movie_data["duration"]} minutes\n'
                    f'Seats available: {movie_data["seats"]}\n'
                    f'Rating: {movie_data["rating"]}\n'
                    f'--- Reviews ---\n{reviews_text}',
                    "Movie Found"
                )
                break
        if not found:
            easygui.msgbox(f'The movie "{title}" does not exist. Please check the name and try again.', "Not Found")
            continue
        return

def addMovie(title, genre, duration, seats):
    title = title.strip()
    for movie_data in movies.values():
        if movie_data["title"].lower() == title.lower():
            easygui.msgbox("Movie is already in the library.", "Error")
            return
    new_key = str(len(movies) + 1)
    movies[new_key] = {
        "title": title,
        "genre": genre,
        "duration": duration,
        "seats": seats,
        "rating": 0,
        "reviews": {},
        "price": 12,
    }
    easygui.msgbox(f'Movie "{title}" added successfully!', "Success")

def addUser():
    while True:
        fields = ["Username", "Password"]
        msg = "Sign up"
        title = "Sign up page"
        loginPage = easygui.multpasswordbox(msg, title, fields)
        if loginPage is None:
            return
        username = loginPage[0].strip()
        password = loginPage[1]
        if not username or not password:
            easygui.msgbox("Please fill in all fields.", "Error")
            continue
        if username in users:
            easygui.msgbox("Username already exists. Choose another username.", "Error")
            continue
        users[username] = {"password": password, "balance": 0.0}
        easygui.msgbox(f"User '{username}' created successfully!", "Success")
        return

def login():
    global current_user
    attempts = 0
    while attempts < 3:
        fields = ["Username", "Password"]
        msg = "Login"
        title = "Login page"
        loginPage = easygui.multpasswordbox(msg, title, fields)
        if loginPage is None:
            return
        username = loginPage[0].strip()
        password = loginPage[1]
        if username in users and users[username]["password"] == password:
            current_user = username
            easygui.msgbox(f"Logged in as {username}", "Success")
            return
        else:
            easygui.msgbox("Incorrect username or password.", "Error")
            attempts += 1
    easygui.msgbox("Too many failed attempts. Returning to startup menu.", "Error")

def buyTicket():
    global current_user
    if current_user is None:
        easygui.msgbox("You must be logged in to buy tickets.", "Error")
        return
    choices = [movies[m]["title"] for m in movies]
    movie_title = easygui.choicebox("Select a movie to buy tickets for:", "Buy Ticket", choices)
    if movie_title is None:
        return
    movie_key = None
    for key, movie_data in movies.items():
        if movie_data["title"] == movie_title:
            movie_key = key
            break
    if movie_key is None:
        easygui.msgbox("Selected movie not found.", "Error")
        return
    seats_available = movies[movie_key]["seats"]
    if seats_available <= 0:
        easygui.msgbox("Sorry, no seats available for this movie.", "Sold Out")
        return
    choices = ["1", "2", "5"]
    ticket_choice = easygui.choicebox(f"{movie_title} has {seats_available} seats available.\nHow many tickets would you like to buy?", "Buy Tickets", choices)
    if ticket_choice is None:
        return
    try:
        tickets_to_buy = int(ticket_choice)
    except ValueError:
        easygui.msgbox("Invalid number of tickets selected.", "Error")
        return
    if tickets_to_buy > seats_available:
        easygui.msgbox(f"Only {seats_available} seats are available. Please choose fewer tickets.", "Error")
        return
    price = movies[movie_key]["price"]
    total_cost = tickets_to_buy * price
    balance = users[current_user].get("balance", 0)
    if balance < total_cost:
        easygui.msgbox(f"Insufficient balance. You need ${total_cost} but have only ${balance}.", "Error")
        return
    users[current_user]["balance"] -= total_cost
    movies[movie_key]["seats"] -= tickets_to_buy
    easygui.msgbox(f"Successfully purchased {tickets_to_buy} ticket(s) for {movie_title}.\nTotal cost: ${total_cost}\nRemaining balance: ${users[current_user]['balance']:.2f}", "Success")

def mainMenu():
    while True:
        options = ["Search movie", "Buy ticket", "Logout", "Exit"]
        choice = easygui.choicebox("What would you like to do?", "Main Menu", options)
        if choice == "Search movie":
            searchMovie()
        elif choice == "Buy ticket":
            buyTicket()
        elif choice == "Logout":
            global current_user
            current_user = None
            easygui.msgbox("You have been logged out.", "Logout")
            return
        elif choice == "Exit" or choice is None:
            exit()
        else:
            easygui.msgbox("Invalid option selected.", "Error")

def adminMenu():
    while True:
        options = ["Add movie", "Search movie", "Buy ticket", "Logout", "Exit"]
        choice = easygui.choicebox("Admin Menu - What would you like to do?", "Admin Menu", options)
        if choice == "Add movie":
            fields = ["Title", "Genre", "Duration (minutes)", "Seats Available"]
            movie_details = easygui.multenterbox("Enter movie details", "Add Movie", fields)
            if movie_details is None:
                continue
            title = movie_details[0]
            genre = movie_details[1]
            try:
                duration = int(movie_details[2])
                seats = int(movie_details[3])
            except ValueError:
                easygui.msgbox("Duration and seats must be numbers.", "Error")
                continue
            addMovie(title, genre, duration, seats)
        elif choice == "Search movie":
            searchMovie()
        elif choice == "Buy ticket":
            buyTicket()
        elif choice == "Logout":
            global current_user
            current_user = None
            easygui.msgbox("You have been logged out.", "Logout")
            return
        elif choice == "Exit" or choice is None:
            exit()
        else:
            easygui.msgbox("Invalid option selected.", "Error")

def startUp():
    while True:
        options = ["Login", "SignUp", "Search movie", "Exit"]
        option = easygui.choicebox("Welcome! What would you like to do?", "Start Menu", options)
        if option == "Login":
            login()
            if current_user is not None:
                if current_user == "admin":
                    adminMenu()
                else:
                    mainMenu()
        elif option == "SignUp":
            addUser()
        elif option == "Search movie":
            searchMovie()
        elif option == "Exit" or option is None:
            exit()
        else:
            easygui.msgbox("Invalid option selected.", "Error")

startUp()
