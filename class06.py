
# ----------------------- Recursive  --------------------------

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(4))

# ----------Towers of honoi ----------------- 

# def printMove(fr, to):
#     print(f"move from {fr} to {to}")

# def Towers(n, fr, to, spare):
#     if n == 1:
#         printMove(fr, to)
    
#     else:
#         Towers(n-1, fr, spare, to)
#         Towers(1, fr, to, spare)
#         Towers(n-1, spare, to, fr)

# Towers(3, 'A', 'C', 'B')


# ---------------fibonacchi --------------

# def fibonacchi(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacchi(n - 1) + fibonacchi(n - 2)

# n = int(input("Enter the fibonacchi number you need : "))
# print(fibonacchi(n))

# ---------------- Sum of digits -------------

# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     return (n % 10) + sum_of_digits(n // 10)

# print(sum_of_digits(1234))

# --------------gcd ---------------

# def gcd(a,b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# print(gcd(48,18)) 

# -------------------- sum of target --------

# def subset_sum(arr, target, index=0):
#     if target == 0:
#         return True
#     if index >= len(arr) or target < 0:
#         return False

#     # Include or exclude current element
#     return subset_sum(arr, target - arr[index], index + 1) or subset_sum(arr, target, index + 1)

# # Test
# arr = [3, 34, 4, 12, 5, 2]
# target = 9
# print(subset_sum(arr, target))  # Output: True


#  -------------palindrome -----------







    



