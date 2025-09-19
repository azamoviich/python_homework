###########
# Homework 1 (Create and Access List Elements)
###########
fruits = ["apple", "banana", "mango", "grape", "orange"]
print("Third fruit:", fruits[2])

###########
# Homework 2 (Concatenate Two Lists)
###########
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Concatenated list:", combined)

###########
# Homework 3 (Extract Elements from a List)
###########
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print("Extracted elements:", new_list)

###########
# Homework 4 (Convert List to Tuple)
###########
movies = ["Inception", "Interstellar", "Matrix", "Avengers", "Batman"]
movies_tuple = tuple(movies)
print("Movies tuple:", movies_tuple)

###########
# Homework 5 (Check Element in a List)
###########
cities = ["London", "Paris", "Berlin", "Tokyo"]
print("Is Paris in list?", "Paris" in cities)

###########
# Homework 6 (Duplicate a List Without Using Loops)
###########
nums = [1, 2, 3]
duplicate = nums * 2
print("Duplicated list:", duplicate)

###########
# Homework 7 (Swap First and Last Elements of a List)
###########
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("After swapping:", nums)

###########
# Homework 8 (Slice a Tuple)
###########
t = (1,2,3,4,5,6,7,8,9,10)
print("Slice 3 to 7:", t[3:8])

###########
# Homework 9 (Count Occurrences in a List)
###########
colors = ["blue", "red", "green", "blue", "yellow", "blue"]
print("Blue count:", colors.count("blue"))

###########
# Homework 10 (Find the Index of an Element in a Tuple)
###########
animals = ("cat", "dog", "lion", "tiger")
print("Index of lion:", animals.index("lion"))

###########
# Homework 11 (Merge Two Tuples)
###########
t1 = (1,2,3)
t2 = (4,5,6)
merged = t1 + t2
print("Merged tuple:", merged)

###########
# Homework 12 (Find the Length of a List and Tuple)
###########
lst = [1,2,3,4]
tpl = (10,20,30)
print("List length:", len(lst))
print("Tuple length:", len(tpl))

###########
# Homework 13 (Convert Tuple to List)
###########
tpl = (5,10,15,20,25)
lst = list(tpl)
print("Converted list:", lst)

###########
# Homework 14 (Find Maximum and Minimum in a Tuple)
###########
nums = (12, 45, 7, 89, 23)
print("Max:", max(nums))
print("Min:", min(nums))

###########
# Homework 15 (Reverse a Tuple)
###########
words = ("python", "java", "c++", "ruby")
print("Reversed tuple:", words[::-1])
