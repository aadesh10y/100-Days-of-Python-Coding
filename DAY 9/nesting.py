capitals = {
    "france": "paris",
    "germany": "berlin",
}

# travel_log = {
#     "france": ["paris", "lille", "marsille"],
#     "germany": ["Berlin", "munich"]
# }

# print(travel_log["france"][1])

nested_list = ["a", "b",["c", "d"]]
# print(nested_list[2][1])

travel_log = {
    "france": {
        "num_times_visited": 2,
        "cities_visited": ["paris", "lille", "marsille"]
        },
    "germany": {
        "num_times_visited": 4,
        "cities_visited": ["Berlin", "Munich"]
    }
}

print(travel_log["germany"]["cities_visited"][1])