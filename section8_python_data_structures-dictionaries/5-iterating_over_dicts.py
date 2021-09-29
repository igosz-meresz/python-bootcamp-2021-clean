# -----------------------------------------------------
# ---------**## Itirating Over Dictionaries ##**-------
# -----------------------------------------------------

# *************------------- Example 29

random = {
    1: 456,
    2: 123,
    45: "Hey",
    "is_employed": False
}

for key in random:
    print(key)

# *************------------- Example 30

employee_info = {
    "Name": "Will",
    "Last Name": "Oldman",
    "Address": "New York, USA",
    "Job": {"Salesperson", "Developer"},
    "Age": 34,
}

for i in employee_info:
    print(employee_info[i])
