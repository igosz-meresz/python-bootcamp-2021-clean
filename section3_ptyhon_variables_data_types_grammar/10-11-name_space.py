# -----------------------------------------------------
# ----------**## Namespace Part 1 ##**-----------------
# -----------------------------------------------------

# *************------------- Example
number = 1001

print(id(number))
print(id(1001))

# *************------------- Example
a = 2
print("a: ", id(a))

a = a + 1
print("a1: ", id(a))
print("Three: ", id(3))

b = 2
print("b:", id(b))
print("Two:", id(2))

# *************------------- Example
something = 12
something = "Jack"
something = ["a", 2, True]

# *************------------- Example


def hello():
    print("Hello Word!")


something = hello
something()

# -----------------------------------------------------
# ----------**## Namespace Part 2 ##**-----------------
# -----------------------------------------------------

# *************------------- Example


def outer():
    outer_number = 100
    print(id(outer_number))

    # this is very bad practice, don't use it
    global global_number
    global_number = 101
    print("Global number =", global_number)

    def inner():
        inner_number = 200
        inner_number = "Jack"
        print("Inner number =", inner_number)

        # see the id, this is a new object =/= the first outer number.
        outer_number = 500
        print("Outer number = ", outer_number)
        # you can access objects from other functions but you cannot modify it
        print(id(outer_number))

    inner()


global_number = 300


outer()
print(global_number)
