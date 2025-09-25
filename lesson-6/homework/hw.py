###########
# Homework 1 (Modify String with Underscores)
###########
def modify_string(txt):
    result = ""
    count = 0
    for i in range(len(txt)):
        result += txt[i]
        count += 1
        if count == 3:
            if txt[i] in "aeiouAEIOU":
                result += txt[i+1] + "_"
                count = 0
                # skip next char because already added
                if i+1 < len(txt):
                    txt = txt[:i+1] + "_" + txt[i+2:]
            else:
                if i != len(txt) - 1:
                    result += "_"
                count = 0
    return result

print(modify_string("hello"))          # hel_lo
print(modify_string("assalom"))        # ass_alom
print(modify_string("abcabcabcdeabcdefabcdefg"))


###########
# Homework 2 (Integer Squares Exercise)
###########
n = int(input("Enter a number: "))
for i in range(n):
    print(i ** 2)


###########
# Homework 3 (Loop-Based Exercises)
###########

# Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Print pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Exercise 3: Sum of numbers
num = int(input("Enter number: "))
s = sum(range(1, num + 1))
print("Sum is:", s)

# Exercise 4: Multiplication table
n = int(input("Enter number for table: "))
for i in range(1, 11):
    print(n * i)

# Exercise 5: Display numbers from list
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num % 5 == 0 and num <= 150:
        print(num)

# Exercise 6: Count digits
num = int(input("Enter a number: "))
print("Total digits:", len(str(num)))

# Exercise 7: Reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Exercise 8: Reverse list
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

# Exercise 9: Display -10 to -1
for i in range(-10, 0):
    print(i)

# Exercise 10: Done message
for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11: Prime numbers in range
start, end = 25, 50
print("Prime numbers between 25 and 50:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 12: Fibonacci up to 10 terms
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()

# Exercise 13: Factorial
num = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"{num}! = {fact}")


###########
# Homework 4 (Return Uncommon Elements of Lists)
###########
def uncommon_elements(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    for y in list2:
        if y not in list1:
            result.append(y)
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))            # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))            # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) # [2, 2, 5]
