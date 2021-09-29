# -----------------------------------------------------
# -------------**## Dictionary Methods ##**------------
# -----------------------------------------------------

employee_info = {
    "Name": "Will",
    "Last Name": "Oldman",
    "Address": "New York, USA",
    "Job": {"Salesperson", "Developer"},
    "Age": 34,
    "Hobbies": ("Reading", "Watching Movies", "Walking"),
    1992: "Date of Birth",
    "Married": True,
    "Favourite Songs": ["Una Dia", "Blinding Lights", "Shallow"],
    "Best Friend": {"Name": "Gerald"},
    "Special One": None
}

# *************------------- Example 8 ->>>>> clear()

# employee_info.clear()
# print(employee_info)

# *************------------- Example 9 ->>>> copy()
gerald_info = employee_info.copy()
gerald_info["Best Friend"] = "Will Oldman"
# print(gerald_info)

# *************------------- Example 10 ->>>> fromkeys()
letters = {'a', 'e', 'i', 'o', 'u'}
numbers = [1, 2, 3]

# vowels = dict.fromkeys(letters)
# vowels = dict.fromkeys(letters, numbers)
# print(vowels)

# print({}.fromkeys(employee_info))

# *************------------- Example 11 ->>>> items()
# print(employee_info.items())

# *************------------- Example 12 ->>>> items()

# del employee_info['Best Friend']
# print(employee_info.items())

# *************------------- Example 13 ->>>> keys()
# print(employee_info.keys())

# *************------------- Example 14 ->>>> keys()
# del employee_info["Hobbies"]
# print(employee_info.keys())

# *************------------- Example 15 ->>>> values()
# print(employee_info.values())

# *************------------- Example 16 ->>>> values()
# del employee_info["Age"]
# print(employee_info.values())

# *************------------- Example 17 ->>>> popitem()
# print(employee_info.popitem())
# print(employee_info)

# *************------------- Example 18 ->>>> setdefault()
# print(employee_info.setdefault("Age"))
# 34

# print(employee_info.setdefault("Smoking"))
# None

# print(employee_info.setdefault("Allergies", "N/A"))
# gets printed

# print(employee_info.setdefault("Name", "Ryan"))
# Will because it's a default argument. If you get rid of Will it'll be changed to Ryan

# print(employee_info)
# It creates the key "Smoking"

# *************------------- Example 19 ->>>> pop()
# Case 1
# target_item1 = employee_info.pop("Age")
# print(target_item1)
# print(employee_info)

# Case 2
# target_item2 = employee_info.pop("Smoking", "No")
# print(target_item2)
# print(employee_info)

# Case 3
# target_item3 = employee_info.pop("Allergies")
# print(target_item3)
# print(employee_info)

# Case 4
# target_item4 = employee_info.pop("Best Friend", "Marcin")
# print(target_item4)
# print(employee_info)

# *************------------- Example 20 ->>>> update()
# Case 1

# lost_key = {"Favourite Movies": "The Blood Diamond"}
# employee_info.update(lost_key)
# print(employee_info)

# Case 2
# found_key = {"Favourite Movies": "Titanic"}
# employee_info.update(found_key)
# print(employee_info)

# Case 3 ->>> when a tuple is passed
employee_info.update(Dog_Name="Krypto", Bird_Name="Precious")
print(employee_info)
