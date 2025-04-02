
# dictionary is something like JS object ---------

# def lyrics_to_frequencies(lyrics):
#     myDict = {}
#     for word in lyrics:
#         if word in myDict:
#             myDict[word] += 1
#         else:
#             myDict[word] = 1
#     return myDict

# # lyrics = ["hello", "world", "hello", "python", "world", "hello"]
# # print(lyrics_to_frequencies(lyrics))

# lyrics = input("Enter the song lyrics : ").split()
# print(lyrics_to_frequencies(lyrics))


#    -------------- Dictionary with fibonacchi --------------

def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans



d = {1:1,
     2:2}
n = int(input("Enter the fibo number : "))
print(fib_efficient(n,d))

