# TODO: Ask the user for an input that should be a number
number = input("Enter number: ")

# TODO: Then try to convert this into an integer using the following:
number_converted = int(number)
print(f"You entered a valid positive integer: {number_converted}")

# The user could provide an invalid integer input (string)
# TODO: Handle this case
invalid_input = True
try:    
    number_converted = int(number)
    invalid_input = False
except:
    print("Invalid input, please provide a valid integer.")
if not invalid_input:
    if number_converted < 0:
        print("The number is negative, please provide a positive integer.")
    else:
        print(f"You entered a valid positive integer: {number_converted}")
        

# The user could give a negative number
# TODO: Handle this case
negative_input = True
if not invalid_input:
    if number_converted < 0:
        print("The number is negative, please provide a positive integer.")
    else:
        negative_input = False
        print(f"You entered a valid positive integer: {number_converted}")
        

# Challenge: TODO: Give the user infinite times to retry
infinite_retry = True
while infinite_retry:
    if not invalid_input and not negative_input:
        infinite_retry = False
    else:
        number = input("Enter number: ")
        try:    
            number_converted = int(number)
            invalid_input = False
        except:
            print("Invalid input, please provide a valid integer.")
            continue
        if number_converted < 0:
            print("The number is negative, please provide a positive integer.")
            continue
        else:
            negative_input = False
            print(f"You entered a valid positive integer: {number_converted}")
            infinite_retry = False
            
