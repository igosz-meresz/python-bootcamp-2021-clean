# -----------------------------------------------------
# --------------**## For Loops 1 ##**------------------
# -----------------------------------------------------

# *************------------- Example 1
print("Success")
print("Success")

# *************------------- Example 2
for x in range(10):
    print(x)

# *************------------- Example 3
for number in range(5):
    print(f"The Code has run for {number} times(s)")

# *************------------- Example 4
for a in range(5, 15):
    print(a)

# *************------------- Example 5
for a in range(0, 100, 10):
    print(a)

# -----------------------------------------------------
# --------------**## For Loops 2 ##**------------------
# -----------------------------------------------------

# *************------------- Example 6
status = True

for number in range(1, 4):
    print(f"Attempt {number}")

    if status:
        print("Success")
        break

# *************------------- Example 7
status = False

for number in range(1, 4):
    print(f"Attempt {number}")

    if status:
        print("Success")
        break
else:
    print("Failed")
