# -----------------------------------------------------
# -------**## Instance vs Class attributes ##**--------
# -----------------------------------------------------

# 1- Instance Attr ->>>> within the constructor
# 2- Class Attr ->>>> within the class itself

# ***********----------- Example 7 ->>>> Instance Attr
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"walking coordinates ({self.x}, {self.y})")


# 1st instantiation
test_walk1 = Robot(8.9, 99.7)
test_walk1.walk()

print(test_walk1.x)
print(test_walk1.y)

# 2nd instantiation
test_walk2 = Robot(4.5, 6.7)
test_walk2.walk()

print(test_walk2.x)
print(test_walk2.y)

# ***********----------- Example 8 ->>>> different Instance Attr
test_walk1.z = 2.3
print(test_walk1.z)

# ***********----------- Example 9 ->>>> Class Attr


class Robot1:
    # a class attribute is going to be shared among all instances of this class
    coordinate_z = 45.87

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"Walking some more coordinates ({self.x}, {self.y})")


# 1st instantiation
test_walk1 = Robot1(8.9, 99.7)
print(test_walk1.coordinate_z)

# 2nd instantiation
test_walk2 = Robot1(4.5, 6.7)
print(test_walk2.coordinate_z)
