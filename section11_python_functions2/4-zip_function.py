# -----------------------------------------------------
# ---------------**## Zip Functions ##**---------------
# -----------------------------------------------------

# *************------------- Example 9
# numbers_list = [1, 2, 3]
# names_list = ["Basia", "Igor", "Mati"]

# No Iterables are passed
# result = zip()

# Converting the Iterator to a list
# result_list = list(result)
# print(result_list)

# # Two iterables are passed
# result = zip(numbers_list, names_list)

# Converting to a set
# result_set = set(result)
# print(result_set)

# *************------------- Example 10 ->>> different number of iterables
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names_list = ['Basia', 'Igor', 'Mati']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX')

# result = zip(numbers_list, numbers_tuple)

# Converting to set
# result_set = set(result)
# print(result_set)

# restult = zip(numbers_list, names_list, numbers_tuple)

# Converting to a list
# result_list = list(result)
# print(result_list)

# *************------------- Example 11 ->>> unzipping the values using the zip()

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

unzipped_coordinates, unzipped_values = zip(*result_list)

# unzipped iterables are converted to a tuple
print("unzipped coordinates:", unzipped_coordinates)
print("unzipped values:", unzipped_values)
