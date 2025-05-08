books = ['1984', 'The Catcher in the Rye', 'To Kill a Mockingbird', 'The Great Gatsby']
print(f"I've read {books[0]} and {books[-1]}.")
books.append("Moby Dick")
books.insert(2, "Pride and Prejudice")
books.remove("The Catcher in the Rye")
books[0] = "Brave New World"

for i in books:
    print(f"I've read {i}.")

more_books = ['The Hobbit', 'Fahrenheit 451']
for i in more_books:
    print(f'I also recommand {i}')