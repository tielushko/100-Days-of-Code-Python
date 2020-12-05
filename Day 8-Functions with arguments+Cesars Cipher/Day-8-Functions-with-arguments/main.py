# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("HELLo")    
    print("HELLo")     
    print("HELLo")

def greet_with_name(name):
    print(f"Hello {name}")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}?")
greet()
greet_with_name("Oleg")
greet_with_name("Angela")
#positional argument example
greet_with("Oleg", "Tampa")

#keyword argument example 
greet_with(location='London', name="Angela")