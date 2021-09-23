# -----------------------------------------------------
# --------------**## String Methods ##**---------------
# -----------------------------------------------------

# 1- len()
address = "Poland"
print(len(address))

# 2- [] Notation
print(address[0])  # P in Poland
print(address[5])  # d in Poland
print(address[-3])  # a in Poland

# 3- [] Notation
print(address[0:4])  # Pola
print(address[:5])  # Polan
print(address[2:])  # land
print(address[:])  # Poland

# 4- Concatonation ->>>>> Formatted Strings
country = "USA"
city = "NYC"
full_address = city + ", " + country
print(full_address)  # NYC, USA

full_address = f"My address is {city}, {country}. It's lovely here."


# 5- upper()
# print(address.upper())

#  6- lower()
# # print(address.lower())

# 7- title()
# print(full_address.title())

# 8- strip()
job = "             Programmer  "
print(job.strip())
print(job)
print(job.lstrip())
print(job.rstrip())

# 9- find()
print(address.find("n"))
print(address.find("o"))

# 10- replace()
print(address.replace("P", "X"))  # Xoland

# 11- in operator
print("ne" in city)
print("ol" in address)

# 12- not operator
print("ne" not in city)
print("ol" not in address)
