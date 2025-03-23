
# x = 10

# def my_function():
#     global x

#     x = 5
#     print('inside function : ',x)

# my_function()
# print('outside function : ', x)


# ----------------------Inner and Outer function -----------

# def outer_function():
#     x = 10

#     def inner_function():
#         x = 20
#         print('inner x : ', x)

#     inner_function()
#     print('outer function : ', x)

# outer_function()


# countdown problem --------------

# def countdown(n):
#     if n == 0:
#         print("Blast off")
    
#     else:
#         print(n)
#         countdown(n - 1)

# countdown(5)

# def fibonacci(n):
#     if n <= 1:
#         return n
    
#     return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Enter the fibonacci number you want : "))
# print(fibonacci(n))



