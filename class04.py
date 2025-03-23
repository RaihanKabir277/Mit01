
# ---------------------------Function ---------------------

"""
input i , is a positive int returns true if i is even otherwise false
"""

# def is_even(i):

#     print("With return")
#     remainder = i % 2
#     return remainder == 0

# n = int(input("Enter a integer number : "))

# print(is_even(n))

# ---------------- more about ----------

# def is_even(i):

#     remainder = i % 2
#     return remainder == 0

# n = int(input("Enter a max integer series of number : "))

# print(f"all of the even number between 0 and {n} : even or odd")

# for i in range(n):
#     if is_even(i):
#         print(i, "even")
#     else:
#         print(i, "odd")

# -----------------------------Function as Arguments -----------------

# def func_a():
#     print('inside func_a')

# def func_b(y):
#     print('inside func_b')
#     return y

# def func_c(z):
#     print('inside func_c')
#     return z()

# print(func_a())

# print(5 + func_b(2))

# print(func_c(func_a))


#------------------------- Scope examples  ------------------------

# def f(y):
#     x = 1
#     x += 1
#     print(x)

#         # answer of the code is x = 2 and x = 5 
# x = 5
# f(x)
# print(x)

    #    ---------------more-----

# def g(y):
#     print(x)
#     print(x + 1)

# x = 5
# g(x)
# print(x)


# ---------python function does not allow this ------------

# def h(y):
#     x += 1


# x = 5
# h(x)
# print(x)


#  ---------------------- Scope details ---------------------

# def g(x):
#     def h():
#         x = 'abc'
    
#     x = x + 1
#     print('g: x =', x)
#     h()
#     return x

# x = 3
# z = g(x)
# print(z)

