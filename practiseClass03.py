# Modify the original cheerleading program so that vowels are shouted in uppercase, and consonants are whispered in lowercase

# letters = "aefhilmnorxAEFHILMNORX"
# words = input("I will cheer for you! Enter a word :")
# times = int(input("Enthusiasm level(1-10) :"))

# for char in words:
#     if char in letters:
#         print("Give me an "+ char.upper() +"! "+char.upper())
#     else:
#         print("Give me an "+ char.lower() +"! "+char.lower())

# for i in range(times):
#     print(words, "!!!")


# problem -2 : Ask the user for a number and count down to "Blast Off!" with an increasing number of exclamation marks.

# number = int(input("Enter a countdown number :"))

# for i in range(number, 0, -1):
#     print(i, "!" * i)

# print("Blast off!!!")

#   ----------------------improve version -----------

# number = int(input("Enter a countdown number :"))

# for i in range(number, 0, -1):
#     name = input("Enter a name : ")
#     # print(str(i) + "!" + name)
#     print(f"{i} ! {name}")

# print("Blast off!!!")

# number = int(input("Enter a max number you want to countdown : "))

# name = []

# for i in range(number):
#     add = input(f"Enter the name for index {i}: ")
#     name.append(add)

# for i in range(number, 0, -1):
#     print(f"{i} --> {name[i-1]}")

# print("BLAST OFF !!!!!")


#   ----------------------    problem 3    -----------

# Take a person's name and print a backward cheer, revealing the name in reverse.

# name = input("Enter your name : ")

# print("lets print your name in reverse order..")

# for char in reversed(name):
#     print(char.upper())

# print("What does it spell ?")

# print(name[: : -1].upper() + "!!!")

# ---------- more improved in problem 3 ----------

# num = int(input("Enter the number for name added : "))

# name = []

# for i in range(num):
#     add = input(f"Enter the name for index {i} : ")
#     name.append(add)

# # for i in range(len(name)):
# #     for char in reversed(name[i]):
# #         print(char.upper())     #print for a single element 
# #     print(" ")


# for i in range(len(name)):
#     print(f"What does it spell for name {i+1} : ")
#     # for char in reversed(name[i]):
#     print(name[i][: : -1].upper())
    
#     print("\n")




# ----------   ----------------  problem 4 -------- ----------

# Convert user input into a coded message by shifting each letter forward in the alphabet (Caesar cipher shift by 1).

message = input("Enter a secret message : ")

coded_message = " "

for char in message:
    if char.isalpha():
        coded_message += chr(ord(char) + 1)
    else:
        coded_message += char

print("your secret coded message is :",coded_message)








