minimum_height =138

# Ask the user for the following inputs
user_height = int(input("Enter your height in cm: "))

# Notify user if they can enter the ride 
can_enter_ride = user_height >= minimum_height
print("You can enter the ride") 

if not can_enter_ride:
    print("Sorry, you have to grow taller before you can ride.")    