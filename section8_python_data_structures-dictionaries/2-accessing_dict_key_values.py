# -----------------------------------------------------
# -------------**## Accesing Key Values ##**-----------
# -----------------------------------------------------

# *************------------- Example 4

employee_info = {
    "Name": "Will",
    "Last Name": "Oldman",
    "Address": "NYC, USA",
    "Job": "Salesperson",
    "Age": 31,
    # "Favourite Color": "Red"
}

print(employee_info["Name"])
print(employee_info["Job"])

# *************------------- Example 5
employee_info["Job"] = "Developer"
employee_info["Hobbies"] = "Reading", "Movies"

print(employee_info)

# *************------------- Example 6
# print(employee_info["Favourite Color"])
# error

# 1- checking whether a key exists

# if "Favourite Color" in employee_info:
#     print("Favourite Color")

# 2- get()
print(employee_info.get("Favourite Color"))
# None instead of error

# *************------------- Example 7
print(employee_info.get("Favourite Color", "Green"))
