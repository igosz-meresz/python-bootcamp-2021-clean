# -----------------------------------------------------
# -----------**## Ternary Operator ##**----------------
# -----------------------------------------------------

score = 75

# *_*_*_*_*_* First Version
if score >= 75:
    print("Passed")
else:
    print("Failed")

# *_*_*_*_*_* Second Version
if score >= 75:
    result = "Passed"
else:
    result = "Failed"
print(result)

# *_*_*_*_*_* Third Version ->>>>> Ternary Operator
result = "Passed" if score >= 75 else "Failed"
print(result)
