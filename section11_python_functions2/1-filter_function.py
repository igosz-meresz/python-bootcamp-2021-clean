# -----------------------------------------------------
# ----------------**## Filter Function ##**------------
# -----------------------------------------------------

# *************------------- Example 1
# Iterable
letters = ['a', 'b', 'c', 'd', 'e', 'i', 'j', 'o']

# Function


def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if (letter in vowels):
        return True
    else:
        return False


filtered_vowels = filter(filter_vowels, letters)
print(filtered_vowels)
print(type(filtered_vowels))

print("The Filtered vowels are:")

for vowel in filtered_vowels:
    print(vowel)

# *************------------- Example 2
random_list = [1, 0, "a", False, True, "0"]

filtered_list = filter(None, random_list)
print("Truthy Values are:")
for value in filtered_list:
    print(value)
