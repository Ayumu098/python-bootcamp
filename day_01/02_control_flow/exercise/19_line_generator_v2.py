"""
    Crete a function line_generator that has a paramaeter number
    and prints the following:
    Line 1
    Line 2
    Line 3
    . . .
    Line number
"""

#Use the fuction once
def line_generator(number):
    for i in range(1, number + 1):
        print(f"Line {i}")
line_generator(4)
        


