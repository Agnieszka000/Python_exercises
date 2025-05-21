# Challenge: Polynomial, Platform: Hack the Box

# You will be given:
# A list of coefficients and an integer.
# The polynomial is constructed as follows: a0 + a1x + a2x2 + ... + a8x8
# You need to evaluate the polynomial at x.

import re

# take in the number
#n = [1,-2,3,-4,5,-6,7,-8,9,5]
n = input()

# Create a list containing all the numbers, to keep minus together with the integers I use a regex:
numbers = re.findall(r'-?\d+', n)

# calculate answer
# Retrieve the last item from the list and save it as x:
x = numbers[-1]

# Remove the x from the list:
numbers.pop()

# Create an empty list for the results for every coefficient:
polynomial_list = []
polynomial_list.append(n[0])

numbers.pop(0)

# Fill the coefficients results list:

i = 1

for a in numbers:
    polynomial_a = int(a) * int(x)**i
    i += 1
    polynomial_list.append(polynomial_a)

# Map the strings in the polynomial_list into integers.
print(f"polynomial list: {polynomial_list}")    
polynomial_list = list(map(int, polynomial_list))

# Sum them
polynomial = sum(polynomial_list)

# print answer
print(f"Polynomial: {polynomial}")