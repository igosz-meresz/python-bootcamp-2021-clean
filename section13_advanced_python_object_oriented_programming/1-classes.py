# -----------------------------------------------------
# ---------------**## Classes ##**---------------------
# -----------------------------------------------------

'''
Object
1- attributes
2- behaviour
'''

'''
--------------------------------
*-*-*-*-*-*-*-*-*-*-*-*- Class
--------------------------------


A class is a blueprint for creating objects.
'''


class Robot:
    pass


'''
--------------------------------
*-*-*-*-*-*-*-*-*-*-*-*- Object / Instance
--------------------------------


An object (instance) is an instantiation of a class
'''
robot_obj = Robot()

print(robot_obj)
print(type(robot_obj))

# ***********----------- Example 1
x = 25
print(type(x))
# class 'int' for creating integers

y = 3.5
print(type(y))
# class of float for creating floating points

z = True
print(type(z))
# class of bool for creating booleans

my_list = [1, 2, 3]
print(type(my_list))
# class of list for creating lists

my_info = {
    "name": "Igor",
    "last name": "Remesz"
}

print(type(my_info))
# class of dict for creating dictionaries

# all of these are objects belonging to a specific class...
# everything in Python is an object
# to create anything you must use classes
