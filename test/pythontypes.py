def add(firstName: str, lastName: str):
    firstName = firstName.capitalize()  # Assign the capitalized string back to firstName
    return firstName + " " + lastName

fname = "7"
lname = "Gates"

name = add(fname, lname)
print(name)  # Print the name
