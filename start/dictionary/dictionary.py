# This file about dictionary 

# make a new dict

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can that you can easily call over and over again."
}

# Retrieving items from dictionary.
# print(programming_dictionary["Function"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Nesting

travel_log_dict = {
    "France": {"visited_city": ["paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"visited_city": ["Berlin", "Hamburg"], "total_visits": 5},
}

# Nesting Dictionary in a List

travel_log_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]

