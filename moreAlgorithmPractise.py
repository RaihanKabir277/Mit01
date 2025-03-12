
# cube = int(input("Enter the cubic value : "))

# epsilon = 0.01
# num_guesses = 0
# low = 0
# high = max(1.0, cube)

# guess = (high + low)/2.0

# while abs(guess ** 3 - cube) >= epsilon:
#     if guess ** 3 < cube:
#         low = guess

#     else:
#         high = guess

#     guess = (high + low) / 2.0
#     num_guesses += 1

# print("number of guesses required = ", num_guesses)
# print(f"the cubic root of {cube} is , {guess}")


#--------------------- Write a program that approximates the square root of a given number using bisection search.---------

# sqr = float(input("Enter the square root of value you want : "))

# epsilon = 0.1
# low = 0
# num_guesses = 0
# high = max(1.0, sqr)

# guess = (high + low) / 2.0

# while abs(guess ** 2 - sqr) >= epsilon:
#     if guess ** 2 < sqr:
#         low = guess

#     else:
#         high = guess
    
#     guess = (high + low) / 2.0
#     num_guesses += 1

# print("Number of guesses nedded = ",num_guesses)
# print(f"The square root of {sqr} is , {guess}")

# ----------------------Find log₂(x) using bisection search.
# (Find y such that 2^y = x)--------------------

# x = float(input("Enter a number to find is logarithm base - 2 value : "))

# epsilon = 0.01
# low = 0
# high = max(1.0, x)
# num_guesses = 0

# guess = (high + low) / 2.0

# while abs(2 ** guess - x) >= epsilon:
#     if 2 ** guess < x:
#         low = guess
    
#     else:
#         high = guess
    
#     guess = (high + low) / 2.0
#     num_guesses += 1


# print("number of guesses required = ", num_guesses)
# print(f"The base 2 logarithm of {x} is {guess}")


#  ----------------- -------------- Write a program to approximate e^x using the Taylor Series Expansion:

# x = float(input("Enter the value of x : "))

# n = int(input("Enter the number of terms : "))

# fact = 1
# power = 1
# result = 1

# for i in range(1, n):

#     fact *= i
#     power *= x

#     result += power / fact 

# print(f"approximate e^{x} = {result}")


# ----------------------------  ----Solve x^5 - 2x^3 + x - 7 = 0 Using Bisection Search------

