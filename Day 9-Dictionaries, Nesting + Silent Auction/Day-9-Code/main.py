programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

# Retrieving items from dictionary
# print(programming_dictionary['Bug'])

# adding new items to dict
# programming_dictionary['loop'] = "the action of doing something over and over again"

# empty dict
# empty_dict = {}

# wipe clear the dict
# programming_dictionary = {}

# modifying ValueError
# programming_dictionary['bug'] = "I hate those with passion..."

# loop through a dictionary
for key in programming_dictionary:
    print(key, programming_dictionary[key])


# simple list
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin'
}

# nested list in dict
travel_log_simple = {
    'France': ['Paris', 'Lille', 'Lyon', 'Marseille'],
    'Germany': ['Berlin', 'Frankfurt', 'Stuttgart', 'Munich']
}

# nested dict in dict
travel_log_complex = {
    'France': {
        'cities_visited': ['Paris', 'Lille', 'Lyon', 'Marseille'],
        'total_visits': 4
        },
    'Germany': {
        'cities_visited': ['Berlin', 'Frankfurt', 'Stuttgart', 'Munich'],
        'total_visits': 4
        } 
} 

# nested dict in list
travel_log_upd = [
    {  
        'country': 'France',
        'cities_visited': ['Paris', 'Lille', 'Lyon', 'Marseille'],
        'total_visits': 4
    },
    {
        'country':'Germany',
        'cities_visited': ['Berlin', 'Frankfurt', 'Stuttgart', 'Munich'],
        'total_visits': 4
    }
]