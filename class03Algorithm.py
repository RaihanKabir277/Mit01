

# cube = int(input("Enter the cube value you want : "))

# for guess in range(abs(cube) + 1):
#     if guess ** 3 >= abs(cube):
#         break
# if guess ** 3 != abs(cube):
#     print(cube, 'is not a perfect cube')
# else:

#     if cube < 0:
#         guess = - guess
    
#     print('cube root of ' + str(cube)+ ' is ' +str(guess))



#  guess and check method algorithm with section searching ...

# cube = int(input("Enter the cubic value you want :"))

# epsilon = 0.01
# num_guesses = 0
# low = 0

# high = cube

# guess = (high + low)/2.0

# while abs(guess ** 3 - cube) >= epsilon:
#     if guess ** 3 < cube:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low) / 2.0
#     num_guesses += 1

# print('number of gueses = ',num_guesses)

# print(f"{guess} is close to the root of {cube}")


# for square root using guess and check method -------------------

# x = float(input("Enter a number to find its square root: "))

# epsilon = 0.01  # Allowed error
# low = 0
# high = max(1.0, x)  # Ensures proper bounds for numbers < 1
# guess = (high + low) / 2.0
# num_guesses = 0

# while abs(guess**2 - x) >= epsilon:
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low) / 2.0
#     num_guesses += 1

# print("Number of guesses:", num_guesses)
# print(f"Approximate square root of {x} is {guess}")



# Find log₂(x) using bisection search.
# (Find y such that 2^y = x)


x = float(input("Enter a number to find its base - 2 logarithm : "))

epsilon = 0.1
low = 0
high = x

guess = (high + low) / 2.0
num_guesses = 0

while abs(2 ** guess - x) >= epsilon:
    if 2 ** guess < x :
        low = guess
    else:
        high = guess
    
    guess = (high + low ) / 2.0
    num_guesses += 1


print("numbber of guesses : ", num_guesses)

print(f"log2({x}) = {guess}")