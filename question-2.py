# Question 2: Borrower information

borrower = ("John Doe", "B1023", "2025-10-15")

print("Borrower details:")
print(borrower)

# Attempt to modify the first element
try:
    borrower[0] = "Jane Doe"
except TypeError as error:
    print("Modification error:", error)

# Display the length of the tuple
print("Number of data fields:", len(borrower))

# Display each element
print("Individual borrower details:")
for detail in borrower:
    print(detail)