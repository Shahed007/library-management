# Question 1: Managing the library book list

books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]

# Add two books
books.append("To Kill a Mockingbird")
books.append("The Great Gatsby")

# Remove the damaged book
books.remove("Moby Dick")

# Sort the list alphabetically
books.sort()

# Display the final list
print("Final list of available books:")
for book in books:
    print(book)