"""
    Crete a function line_generator that prints the following:
    Line 1
    Line 2
    Line 3
    . . .
    Line number
"""

#Use the fuction once
def line_generator():
    line_number = int(input("Enter a number: "))
    for i in range(1, line_number + 1):
        print(f"Line {i}")
line_generator()

