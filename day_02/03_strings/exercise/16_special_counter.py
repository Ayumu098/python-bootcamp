password = input("Enter password: ")

lower_case_count = 0
upper_case_count = 0

for letter in password:
    if letter.islower():
        lower_case_count += 1
    elif letter.isupper():
        upper_case_count += 1

print(lower_case_count)
print(upper_case_count)