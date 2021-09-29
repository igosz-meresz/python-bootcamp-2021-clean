# -----------------------------------------------------
# -----------**## Dictionary Comprehensions ##**------------
# -----------------------------------------------------

# *************------------- Example 21
# coordinates = {}

# for x in range(5):
#     coordinates[x] = ((x * 5) / 2 + 12) - (2.4 / 1.2) * 6

# print(coordinates)

# *************------------- Example 22
coordinates = {x: ((x * 5) / 2 + 12) - (2.4 / 1.2) * 6 for x in range(5)}

print(coordinates)

# *************------------- Example 23

# items prices in Dollars
old_price = {"milk": 1.02, "coffee": 2.5, "bread": 1.89}

dollar_to_pund = 0.76
new_price = {item: value *
             dollar_to_pund for (item, value) in old_price.items()}

print(new_price)

# *************------------- Example 24 ->>> If Conditional Dictionary Example
original_dict = {'Jack': 38, 'Lincoln': 48,
                 'Theodore': 57, 'John': 33, "Cecile": 21, "Tony": 18}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)

# *************------------- Example 24 ->>>> Multiple if Conditional Dictionary Comprehension
original_dict = {'Jack': 38, 'Lincoln': 48,
                 'Theodore': 57, 'John': 33, "Cecile": 21, "Tony": 18}

# new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
# print(new_dict)

# *************------------- Example 25 ->>>> if-else conditional dictionary comprehension
# new_dict = {k: "old" if v > 40 else "young" for (k, v) in original_dict.items()}
# print(new_dict)

# *************------------- Example 26 ->>>> Nested Dictionary with Two Dictionary Comprehensions
# new_dict = {
#     k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
# }

# print(new_dict)

# *************------------- Example 27 ->>>> Nested Dictionary with Two Dictionary Comprehensions in the loop form
# new_dict = {}
# for k1 in range(2, 5):
#     new_dict[k1] = {k2: k1 * k2 for k2 in range(1, 6)}

# print(new_dict)

# *************------------- Example 28 ->>> Nested Dictionary with Two Dictionary Comprehensions in the loop form, completely unfolded
new_dict = {}
for k1 in range(2, 5):
    new_dict[k1] = {}
    for k2 in range(1, 6):
        new_dict[k1][k2] = k1 * k2

print(new_dict)
