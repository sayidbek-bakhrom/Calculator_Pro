# calculator

# logo for pro

project_logo = """
 _____________________
|  _________________  |
| |created by PYTHON| |   
| |_________________| | 
|  ___ ___ ___   ___  | 
| | 7 | 8 | 9 | | + | | 
| |___|___|___| |___| | 
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| | 
| | . | 0 | = | | / | | 
| |___|___|___| |___| |   
|_____________________|
"""


print(project_logo)


# creating functions of operation
def add(k1, k2):
    return k1 + k2

def subtract(k1, k2):
    return k1 - k2

def multiply(k1, k2):
    return k1 * k2

def divide(k1, k2):
    return k1 / k2

# storing them in operation


operations = {
    "+": add,
    "-": subtract,
    "x": multiply,
    "/": divide,
}



# checking functions
# function = operations["-"]

number1 = float(input("Enter the number: "))

for key in operations:
    print(key)

continuing = True
while continuing:
    chosen_key = input("Choose one above operation: ")
    number2 = float(input("Enter another number: "))
    function = operations[chosen_key]
    answer = round(function(number1, number2), 3)

    print(f"{number1} {chosen_key} {number2} = {answer}")


    if input(f"Hit 'y' to go on with {answer}, or 'n' to stop ") == "y":
        number1 = answer

    else:
        continuing = False


# function = operations[chosen_key]
answer = function(number1, number2)

print(f"{number1} {chosen_key} {number2} = {answer}")

