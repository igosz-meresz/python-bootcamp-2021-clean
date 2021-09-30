# -----------------------------------------------------
# ----------------**## More Set Methods ##**-----------
# -----------------------------------------------------

# *************------------- Example 24 ->>>> copy()
numbers = {101, 202, 303, 404, 505, 606}
other_numbers = numbers
# print(numbers)
# print(other_numbers)

# numbers.remove(606)
# print(numbers)
# print(other_numbers)

# other_numbers.discard(505)
# print(other_numbers)
# print(numbers)

some_numbers = numbers.copy()
print(some_numbers)
print(numbers)

some_numbers.add(909)
print(numbers)
print(some_numbers)

print(id(numbers))
print(id(some_numbers))
print(id(other_numbers))


# *************------------- Example 25 ->>>> isdisjoint() with sets
A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}
D = {10, 20, 30, 7}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and B disjoint?', A.isdisjoint(C))
print('Are A and B disjoint?', B.isdisjoint(C))
print('Are A and B disjoint?', A.isdisjoint(D))
print('Are A and B disjoint?', B.isdisjoint(D))
print('Are A and B disjoint?', C.isdisjoint(D))

# *************------------- Example 26 ->>>> isdisjoint() with other iterables
A = {'a', 'b', 'c', 'd'}
B = ['b', 'e', 'f']
C = '5de4'
D = {1: 'a', 2: 'b'}
E = {'a': 1, 'b': 2}
F = ("z", "g", "s")

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and B disjoint?', A.isdisjoint(C))
print('Are A and B disjoint?', A.isdisjoint(D))
print('Are A and B disjoint?', A.isdisjoint(E))
print('Are A and B disjoint?', A.isdisjoint(F))

# -----------------------------------------------------
# ---------------**## More Set Methods 2 ##**----------
# -----------------------------------------------------

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

# *************------------- Example 27 ->>>> issubset()

print(A.issubset(B))
print(A.issubset(C))
print(B.issubset(A))
print(B.issubset(C))
print(C.issubset(A))
print(C.issubset(B))

# *************------------- Example 28 ->>>> issuperset()
print(A.issuperset(B))
print(A.issuperset(B))
print(B.issuperset(A))
print(B.issuperset(C))
print(C.issuperset(A))
print(C.issuperset(B))
