from art import logo
# add operation 
def add(n1, n2):
    return n1 + n2

# subtract operation
def subtract(n1, n2):
    return n1 - n2

# divide operation
def divide(n1, n2):
    return n1 / n2

# multiply operation
def multiply(n1, n2):
    return n1 * n2


# store functions in a dict to be called based on the key user enters
operations_dict = {
    '+': add,
    '-': subtract, 
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)
    # flag to continue the game
    do_continue = True


    # pick the first number
    num1 = float(input('What is the first number?\n'))

    # pick the operation
    for operation_char in operations_dict:
        print(operation_char)

    while do_continue:
        operation_choice = input('Pick an operation: (+, -, *, /)\n')

        # pick the second number
        num2 = float(input('What is the next number?\n'))

        # get the operation function from dict
        operation =  operations_dict[operation_choice]

        # perform calculation and store in result
        result = operation(num1, num2)

        # print out the entire operation
        print(f"{num1} {operation_choice} {num2} = {result} ")

        continued = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'q' to exit\n")
        if continued == 'n':
            do_continue = False
            calculator()
        elif continued == 'q':
            do_continue = False
        else:
            num1 = result


calculator()