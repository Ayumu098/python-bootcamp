# TODO: Ask the user for an input
user_choice = input("Pick a choice (rock/paper/scissors): ")
input_choices = ["rock", "paper", "scissors"] 
if user_choice not in input_choices:
    print("Invalid choice, please pick rock, paper, or scissors.")
    exit()


# TODO: Make a random choice for the computer
# Note: Read the slide for this part
import random
cpu_choice = random.choice(input_choices)
print(f"Computer picked: {cpu_choice}") 


# TODO: Determine if the user wins, the cpu wins, or its a draw
if user_choice == cpu_choice:
    print("It's a draw!")
elif (user_choice == "rock" and cpu_choice == "scissors") or \
     (user_choice == "paper" and cpu_choice == "rock") or \
     (user_choice == "scissors" and cpu_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")
    

# Challenge: TODO: Robust Input
robust_input = True
while robust_input:
    if user_choice in input_choices:
        robust_input = False
    else:
        user_choice = input("Pick a choice (rock/paper/scissors): ")
        if user_choice not in input_choices:
            print("Invalid choice, please pick rock, paper, or scissors.")
            continue
        else:
            robust_input = False
            
# Challenge: TODO: Multi-rounds
multi_rounds = True
rounds = int(input("How many rounds do you want to play? "))
current_round = 1
while multi_rounds:
    print(f"Round {current_round} of {rounds}")
    user_choice = input("Pick a choice (rock/paper/scissors): ")
    if user_choice not in input_choices:
        print("Invalid choice, please pick rock, paper, or scissors.")
        continue
    cpu_choice = random.choice(input_choices)
    print(f"Computer picked: {cpu_choice}")
    if user_choice == cpu_choice:
        print("It's a draw!")
    elif (user_choice == "rock" and cpu_choice == "scissors") or \
         (user_choice == "paper" and cpu_choice == "rock") or \
         (user_choice == "scissors" and cpu_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    current_round += 1
    if current_round > rounds:
        multi_rounds = False
