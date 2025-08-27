###########
# Homework 1 (Sort a Dictionary by Value)
###########
sample_dict = {2: 30, 1: 20, 0: 10}
asc = dict(sorted(sample_dict.items(), key=lambda x: x[1]))
desc = dict(sorted(sample_dict.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)

###########
# Homework 2 (Add a Key to a Dictionary)
###########
d = {0: 10, 1: 20}
d[2] = 30
print("Updated dictionary:", d)

###########
# Homework 3 (Concatenate Multiple Dictionaries)
###########
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged = {**dic1, **dic2, **dic3}
print("Concatenated dictionary:", merged)

###########
# Homework 4 (Generate a Dictionary with Squares)
###########
n = 5
squares = {}
for x in range(1, n+1):
    squares[x] = x * x
print("Squares dictionary:", squares)

###########
# Homework 5 (Dictionary of Squares 1 to 15)
###########
squares_15 = {x: x*x for x in range(1, 16)}
print("Squares from 1 to 15:", squares_15)

###########
# Homework 6 (Create a Set)
###########
my_set = {1, 2, 3}
print("Set:", my_set)

###########
# Homework 7 (Iterate Over a Set)
###########
for item in my_set:
    print("Item:", item)

###########
# Homework 8 (Add Member(s) to a Set)
###########
my_set.add(4)
my_set.update([5, 6])
print("After adding:", my_set)

###########
# Homework 9 (Remove Item(s) from a Set)
###########
my_set.remove(2)
print("After removing 2:", my_set)

###########
# Homework 10 (Remove an Item if Present in the Set)
###########
my_set.discard(10)  # does nothing if item not present
print("After discard 10:", my_set)
