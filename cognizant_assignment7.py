# ---------------------------------------
# Task 1 - Working with Lists
# ---------------------------------------

# Create a list of favorite fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Original list:", fruits)

# Append a new fruit
fruits.append('fig')
print("After adding a fruit:", fruits)

# Remove one fruit using remove()
fruits.remove('apple')
print("After removing a fruit:", fruits)

# Print the list in reverse using slicing
print("Reversed list:", fruits[::-1])

print("\n")


# ---------------------------------------
# Task 2 - Exploring Dictionaries
# ---------------------------------------

# Create a dictionary with basic info
my_info = {
    "name": "Alice",
    "age": 25,
    "city": "Seattle"
}

# Add a new key-value pair
my_info["favorite color"] = "Blue"

# Update the city
my_info["city"] = "New York"

# Print all keys and values
print("Keys:", ", ".join(my_info.keys()))
print("Values:", ", ".join(str(value) for value in my_info.values()))

print("\n")


# ---------------------------------------
# Task 3 - Using Tuples
# ---------------------------------------

# Create a tuple of favorite things
favorites = ("Inception", "Bohemian Rhapsody", "1984")
print("Favorite things:", favorites)

# Try to change one element (commented out to avoid crash)
try:
    favorites[0] = "Interstellar"
except TypeError:
    print("Oops! Tuples cannot be changed.")

# Print length of the tuple
print("Length of tuple:", len(favorites))
