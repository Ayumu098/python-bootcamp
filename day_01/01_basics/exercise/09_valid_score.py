# Range minimum and maximum bounds
min_score = 0
max_score = 100

# ENter user input
number = int(input("Enter your score: "))   

# Notify user if the number is a valid score
valid_score = min_score <= number <= max_score
print("Valid score:", valid_score)  