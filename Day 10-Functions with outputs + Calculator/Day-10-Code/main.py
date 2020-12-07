# format string as title

def format_as_title(first_name, last_name):
    """Takes a first and last name and format it to have the first letter uppercase"""
    if first_name == "" or last_name == "":
        return "You didn't provide valid first name or last name"
    format_first = first_name.title()
    format_last = last_name.title()
    return f"{format_first} {format_last}"


print(format_as_title(input("What is your first name?\n"), input("What is your last name?\n")))