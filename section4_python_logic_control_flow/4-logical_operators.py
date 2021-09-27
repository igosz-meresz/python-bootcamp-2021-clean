# -----------------------------------------------------
# -----------**## Logical Operators ##**---------------
# -----------------------------------------------------

"""
1- and
2- or 
3- not
"""
# *************------------- Example ->>>>> AND
high_income = True
good_credit = False

if high_income and good_credit:
    print("Eligible For Loan")
else:
    print("Not Eligible For Loan")

# *************------------- Example ->>>>> OR
high_income = True
good_credit = False

if high_income or good_credit:
    print("Eligible For Loan")
else:
    print("Not Eligible For Loan")

# *************------------- Example ->>>>> NOT
high_income = True
good_credit = True
student = True

if not student:
    print("Eligible For Loan")
else:
    print("Not Eligible For Loan")
