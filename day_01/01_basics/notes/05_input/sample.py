password = input("Enter your password: ")
while password != "pass":
    print("Incorrect password, try again.")
    password = input("Enter your password: ")
    
    
def greetings(name):
    print(f"Hello name ! Nice to meet you.")
   
greetings(name)

def product(x, y, z=1):
    result = x * y * z
    print(f"The product is: {result}")


def product(x, y, z=1):
    result = x * y * z
    return result

output = product(x=1, y=2, z=3) * 5
print(f"The product is: {output}")


try:
    number_input = int(input("Number:"))
except:
    print("Invalid input")
