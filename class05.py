
#  -------------------  Tuples ------------------

# def quotient_and_remainder(x,y):

#     q = x // y
#     r = x % y

#     return(q, r)


# (quot, rem) = quotient_and_remainder(4,5)

# print(quot, rem)


# ------------ create a iterate over tuples -------------

# def get_data(aTuple):
#     nums = ()
#     words = ()

#     for i in aTuple:
#         nums = nums + (i[0],)
#         if i[1] not in words:
#             words = words + (i[1],)

#     min_n = min(nums)
#     max_n = max(nums)

#     unique_words = len(words)

#     return(min_n, max_n, unique_words)


# tSwift = ((2014, "katy"),
#           (2014, "harry"),
#           (2012, "jake"),
#           (2010, "taylor"),
#           (2008, "joe"))

# (mi, ma, numPeople) = get_data(tSwift)

# print(f"from {mi} to {ma} taylor swift wrote song about {numPeople} people")


#  ------ improve version --------------


# def get_data(aTuple):
#     nums = ()
#     words = ()

#     for i in aTuple:
#         nums = nums + (i[0],)
#         if i[1] not in words:
#             words = words + (i[1],)

#     min_n = min(nums)
#     max_n = max(nums)

#     unique_words = len(words)

#     return(min_n, max_n, unique_words)


# n = int(input("Enter the number of entries you want : "))

# tSwift = []

# for i in range(n):
#     year = int(input(f"Enter year for entry{i + 1} : "))
#     name = input(f"Enter name for entry{i + 1} : ")
#     tSwift.append((year, name))

# tSwift = tuple(tSwift)

# (mi, ma, numPeople) = get_data(tSwift)

# print(f"from {mi} to {ma} taylor swift wrote song about {numPeople} people")

#    ------------------ different skim for take tupple input from users -----------------------------------

# a = input("enter elements separated by spaces : ").split()

# t = tuple(a)
# print(t)

# ---- another way -----

# t = tuple(map(int, input("Enter elements separated by spaces : ").split()))
# print(t)

#  -----another way ---------

# Direct tuple input
# t = eval(input("Enter a tuple: "))  # Ex: (1, 2, 3)
# print(t)


# ----------------- using of map() function --------

# def square(x):
#     return x * x

# num = [1, 2, 3, 4, 5]

# result = list(map(square,num))
# print(result)

#  ------------using ananymous lambda function to make it more easy -----

# numbers = [1, 2, 3, 4, 5]

# squared = map(lambda x: x ** 2, numbers)

# print(list(squared))



#  ------------------------------ List -------------------------------

# s = "I<3 cs"
# l = list(s)
# print(l)
# print(s.split('<'))

# l = ['a', 'b', 'c']
# j = ''.join(l)
# print(j)

# underScore = '_'.join(l)
# print(underScore)

#  -------------sort ----------

# L = [9,6,0,3]
 
# L2 = sorted(L)  #here L will remain same create a copy version of L and assign it into L2

# print(L2)

# l = [9,6,0,3]
# l.sort()
# print(l)
# # it will change the l value and being sorted

# l.reverse()
# print(l)


# -----------------Aliases --------------

# warm = ['red', 'yellow', 'orange']

# hot = warm
# hot.append('pink')

# print(hot)
# print(warm)


# for coping something from a list we have to be cloned this ------

# cool = ['blue', 'green', 'grey']
# chill = cool[:]

# chill.append('black')
# print(chill)
# print(cool)

warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]
brightcolors.append(hot)

print(brightcolors)
hot.append('pink')
print(hot)
print(brightcolors)