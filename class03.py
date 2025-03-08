
#    ----------- --------- ------------ String ---------- ------- ----------

# s = "abc"
# print(len(s))

# s = "abc"

# s[0] = "a"
# s[1] = "b"
# s[2] = "c"

# s[-1] = "c"
# s[-2] = "b"
# s[-3] = "a"


#    ----------- --------- ------------slicing into String ---------- ------- ----------

# s = "abcdefgh"
# print(s[3:6]) same as print(s[3:6:1])

# print(s[3:6:2])

# print(s[: :])   same as s[0: len(s)+1: 1]

# print(s[: :-1]) same as s[-1: -len(s) + 1: -1]

# print(s[4:1:-2])

#    ----------- --------- ------------slicing into String ---------- ------- ----------

# s = "hellow"

# s[0] = "y"     # this is not working because string are immutable that means not modifying access

# s = "y" + s[1:len(s)]   #but this is working and allowed
# print(s)

# s = s[0:2] + "bb" + s[4:6]
# print(s)


#    ----------- --------- -----------------String in for loop ---------- ------- ----------


# s = "abcdefgh"

# for char in s:
#     if char == "i" or char == "u":
#         print("there is an i or u") 

#    ----------- --------- -----------------String practise enthusias in for loop ---------- ------- ----------

# an_letters = "aefhilmnorxAEFHILMNORX"

# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1 - 10) :"))

# i = 0

# while i<len(word):
#     char = word[i]
#     if char in an_letters:
#         print("Give me an "+ char +"! "+ char)
#     else:
#         print("Give me a "+ char +"! "+ char)
#     i += 1

# print("What does that spell? ")

# for i in range(times):
#     print(word, "!!!")

#     ----------- ======= if we use for loops instead of while ---------

an_letters = "aefhilmnorxAEFHILMNORX"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1 - 10) :"))

for char in word:
    
    if char in an_letters:
        print("Give me an "+ char +"! "+ char)
    else:
        print("Give me a "+ char +"! "+ char)
   

print("What does that spell? ")

for i in range(times):
    print(word, "!!!")

