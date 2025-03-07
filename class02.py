
# hi = "Hello there"
# name = "Kabir"

# greet = hi + name

# print(greet)

# greeting = hi + " " + name
# print(greeting)

# silly = hi + (" " + name)*3
# print(silly)


# Branching and iteration

# text = input("type anything : ")
# print(5 * (" " + text))

# num = int(input("Type a number :"))
# print(5*num)

# so if we want to print somwething 5 times we have to give the input as a string 

# compare 

# comp = "a" > "b"
# print(comp)

# comp2 = 5 > 2
# print(comp2)

# condition ...

# x = float(input("Enter a number for x :"))
# y = float(input("Enter a number for y :"))

# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("Therefore, x/y is", x/y)

# elif x < y: 
#     print("x is smaller")

# else:
#     print("y is samaller")

# print("thanks")


# n = input("you are the lost forest ........go left or right : ")

# while n == "right" or n == "Right":
#     n = input("you are the lost forest ........go left or right : ")

# print("\n you got out of the forest!")

# -------- -------- === ----------- ====---\

# n = 0
# while n < 5:
#     print(n)
#     n = n + 1
# print("\n")
# for i in range(5):
#     print(i)

# for loop more -----------

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)

#    ---------------   ======= -------------

# for i in range(len(fruits)):
#     x = adj[i]
#     y = fruits[i]
#     print(x, y)

#  ---------- =========== --------------

# for x,y in zip(adj, fruits):
#     print(x, y)

# ----------- ========-=---------------

from itertools import zip_longest

adj = ["red", "big", "tasty", "juicy"]
fruits = ["apple", "banana", "cherry"]

for x, y in zip_longest(adj, fruits, fillvalue="(no fruit)"):
    print(x, y)


