# -----------------------------------------------------
# -------------**## Keyword Arguments ##**-------------
# -----------------------------------------------------

# *************------------- Example 13
def employee(**info):
    print(info)


employee(name="Mati", last_name="Otulak", age=26, skill_set="Graphic Designer")

# *************------------- Example 14


def to_do(**to_do_status):
    return to_do_status


to_do_status = to_do(get_coffee="done", Exercise="pending",
                     watch_tv="in progress")
print(to_do_status)
