# we work with dictionary and we append new item in dict and list

travel_log = [
    {
        "country": "France",
        "city_visited": ["Paris", "Little", "Dijon"],
        "total_visited": 12,
    },
    {
        "country": "Germany",
        "city_visited": ["Hamburg", "Berlin", "stuttgart"],
        "total_visited": 5
    }
]

# TODO - Create a new function to add new country to travel_log

def add_new_country(country, city_visited, total_visited):
    travel_log.append({"country": country, "city_visited": city_visited, "total_visited":total_visited})


add_new_country(country="Russia", total_visited=2, city_visited=["Moscow", "Saint Petersburg"])
print(travel_log)
