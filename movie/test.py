    elif x == "4":
        if adminPerms is True: 
            print("Adding new movie...")
            title = input("Movie name: ")
            genre =input("Movie genre: ")
            duration =input("Movie duration: ")
            seats =input("Movie seats: ")
            addmovie(title, genre,duration,seats)
            print(movies)
        else:
            input("You need to be an admin to use this...")
            startUp()