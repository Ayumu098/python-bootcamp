def product():
    """ TODO: Takes three inputs (or two) and return"""

# TODO: product(1, 1, 1)	# 1
# TODO: product(1, 2, 3)	# 6
# TODO: product(2, 5, 10)	# 100
# TODO: product(3, 3)	    # 9
# TODO: product(2, 5)	    # 12

product1 = int(input("Enter first number: "))
product2 = int(input("Enter second number: "))      
product3 = int(input("Enter third number: "))       
def product(num1, num2, num3=1):
    result = num1 * num2 * num3     
    return result   
output = product(product1, product2, product3) * 5
print(f"The product is: {output}")

