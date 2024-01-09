# import my custom math module
import mymath
# Perform basic math operations
a = 10
b = 3

sum_result = mymath.add(a, b)
difference_result = mymath.minus(a, b)
product_result = mymath.multiply(a, b)
try:
    quotient_result = mymath.divide(a, b)
except ValueError as e:
    quotient_result = str(e)

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
