
###########
# Homework 1 (Check Leap Year Function)
###########
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage
print(is_leap(2000))  # True
print(is_leap(1900))  # False
print(is_leap(2024))  # True


###########
# Homework 2 (Conditional Statements Exercise)
###########
n = int(input("Enter a number (1–100): "))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")


###########
# Homework 3 (Find Even Numbers Between a and b, Inclusive)
###########

# Solution 1 (with if-else)
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a % 2 != 0:   # make 'a' even if it's odd
    a += 1

evens = list(range(a, b + 1, 2))
print("Even numbers (with if-else):", evens)

# Solution 2 (without if-else)
a = int(input("Enter a: "))
b = int(input("Enter b: "))

evens = list(range(a + a % 2, b + 1, 2))
print("Even numbers (without if-else):", evens)
